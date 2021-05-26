#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""AirCotProxy Functions."""

import csv
import datetime
import platform

import xml.etree.ElementTree

import aircot
import pytak

import aircotproxy

__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"



def cot_to_cot_xml(cot: dict, known_craft: dict = {}) -> str:  # NOQA pylint: disable=too-many-locals
    """
    Given an input CoT XML Event with an ICAO Hex as the UID, will transform the Event's name, callsign & CoT Event
    Type based on known craft input database (CSV file).
    """
    uid = str(cot.attrib["uid"]).strip().upper()

    if "ICAO" not in uid:
        return

    if "ICAO-" in uid:
        icao = uid.split("-")[-1]
    elif "ICAO." in uid:
        icao = uid.split(".")[-1]

    name, callsign = aircot.set_name_callsign(icao, "", "", "", known_craft)
    print(name, callsign)
    category = aircot.set_category("", known_craft)
    cot_type = aircot.set_cot_type(icao, category, "", known_craft)

    cot.set("type", cot_type)

    cot_uid = xml.etree.ElementTree.Element("UID")
    cot_uid.set("Droid", name)

    contact = xml.etree.ElementTree.Element("contact")
    contact.set("callsign", str(callsign))

    detail = cot.find("detail")
    cot.remove(detail)
    detail.set("uid", name)

    detail.remove(detail.find("UID"))
    detail.append(cot_uid)

    detail.remove(detail.find("contact"))
    detail.append(contact)

    cot.append(detail)

    return cot


def cot_to_cot(craft: dict, known_craft: dict = {}) -> str:
    """
    Given an input CoT XML Event with an ICAO Hex as the UID, will transform the Event's name, callsign & CoT Event
    Type based on known craft input database (CSV file).
    """
    return xml.etree.ElementTree.tostring(cot_to_cot_xml(craft, known_craft))

