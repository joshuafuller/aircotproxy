#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""AirCoTProxy Function tests."""

import asyncio
import csv
import io
import urllib
import xml.etree.ElementTree

import pytest

import aircotproxy

import aircotproxy.functions


__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"


@pytest.fixture
def sample_data_xml():
    sample_cot = (
        '<event version="2.0" type="a-n-A-C-F" uid="ICAO-A82C75" how="m-g" time="2021-05-26T18:14:45.248507Z" '
        'start="2021-05-26T18:14:45.248507Z" stale="2021-05-26T18:16:45.248507Z"><point lat="38.193146" '
        'lon="-122.48341" ce="66.57" le="22.5" hae="1333.5" /><detail uid="ICAO-A82C75" remarks="N6259T-N6259T- '
        'ICAO: A82C75 REG: N6259T Flight: N6259T Type:  Squawk: 4571 Category: 1 (via stratuxcot@rorqual)">'
        '<UID Droid="ICAO-A82C75" /><contact callsign="N6259T-N6259T-" /><track course="321" speed="69.44994" />'
        '<remarks>N6259T-N6259T- ICAO: A82C75 REG: N6259T Flight: N6259T Type:  Squawk: 4571 Category: 1 '
        '(via stratuxcot@rorqual)</remarks></detail></event>')
    rx_cot = xml.etree.ElementTree.fromstring(sample_cot)
    return rx_cot


@pytest.fixture
def sample_known_craft():
    sample_csv = """DOMAIN,AGENCY,REG,CALLSIGN,TYPE,MODEL,HEX,COT,TYPE,,
EMS,CALSTAR,N832CS,CALSTAR7,HELICOPTER,,,a-f-A-C-H,HELICOPTER,,
EMS,REACH AIR MEDICAL,N313RX,REACH16,HELICOPTER,,,a-f-A-C-H,HELICOPTER,,
FED,USCG,1339,C1339,FIXED WING,,,,FIXED WING,,
FIRE,USFS,N143Z,JUMPR43,FIXED WING,DH6,,a-f-A-C-F,FIXED WING,,
FIRE,,N17085,TNKR_911,FIXED WING,,,a-f-A-C-F,FIXED WING,,
FIRE,CAL FIRE,N481DF,C_104,HELICOPTER,,,a-f-A-C-H,HELICOPTER,,
FOOD,EL FAROLITO,N739UL,TACO_01,HELICOPTER,,A82C75,a-f-A-T-A-C-O,HELICOPTER,,
FOOD,EL FAROLITO,DAL1352,TACO_02,FIXED WING,,,a-f-A-T-A-C-O,FIXED WING,,
"""
    csv_fd = io.StringIO(sample_csv)
    all_rows = []
    reader = csv.DictReader(csv_fd)
    for row in reader:
        all_rows.append(row)
    return all_rows


def test_cot_to_cot_xml_with_known_craft(sample_data_xml, sample_known_craft):
    known_craft_key = "HEX"

    uid = str(sample_data_xml.attrib["uid"]).strip().upper()

    if "ICAO-" in uid:
        filter_key = uid.split("-")[-1].strip().upper()
    elif "ICAO." in uid:
        filter_key = uid.split(".")[-1].strip().upper()

    known_craft = (list(filter(
        lambda x: x[known_craft_key].strip().upper() == filter_key, sample_known_craft)) or
                   [{}])[0]

    cot = aircotproxy.functions.cot_to_cot_xml(sample_data_xml, known_craft)

    assert isinstance(cot, xml.etree.ElementTree.Element)
    assert cot.tag == "event"
    assert cot.attrib["version"] == "2.0"
    assert cot.attrib["type"] == "a-f-A-T-A-C-O"
    assert "ICAO-A82C75" == cot.attrib["uid"]

    point = cot.find("point")
    assert "point" == point.tag
    assert "38.193146" == point.attrib["lat"]
    assert "-122.48341" == point.attrib["lon"]
    assert "1333.5" == point.attrib["hae"]

    detail = cot.find("detail")
    assert "detail" == detail.tag
    assert "TACO_01" == detail.attrib["uid"]

    contact = detail.find("contact")
    assert "contact" == contact.tag
    assert "TACO_01" == contact.attrib["callsign"]

    UID = detail.find("UID")
    assert "UID" == UID.tag
    assert "TACO_01" == UID.attrib["Droid"]

    track = detail.find("track")
    assert "321" == track.attrib["course"]
    assert "69.44994" == track.attrib["speed"]