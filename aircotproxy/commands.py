#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""AirCotProxy Commands."""

import argparse
import asyncio
import collections
import concurrent
import configparser
import logging
import os
import sys
import urllib

import aircot
import pytak

import aircotproxy

# Python 3.6 support:
if sys.version_info[:2] >= (3, 7):
    from asyncio import get_running_loop
else:
    from asyncio import _get_running_loop as get_running_loop


__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"


async def main(opts):
    loop = get_running_loop()
    tx_queue: asyncio.Queue = asyncio.Queue()
    rx_queue: asyncio.Queue = asyncio.Queue()
    cot_url: urllib.parse.ParseResult = urllib.parse.urlparse(opts.get("COT_SEND_URL"))

    # Create our CoT Event Queue Worker
    reader, writer = await pytak.protocol_factory(cot_url)
    write_worker = pytak.EventTransmitter(tx_queue, writer)
    read_worker = pytak.EventReceiver(rx_queue, reader)

    message_worker = aircotproxy.ACPWorker(tx_queue, opts)

    await tx_queue.put(pytak.hello_event("aircotproxy"))

    done, pending = await asyncio.wait(
        set([message_worker.run(), read_worker.run(), write_worker.run()]),
        return_when=asyncio.FIRST_COMPLETED)

    for task in done:
        print(f"Task completed: {task}")


def cli():
    """Command Line interface for AIS Cursor-on-Target Gateway."""

    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--CONFIG_FILE", dest="CONFIG_FILE", default="config.ini", type=str)
    parser.add_argument(
        "-d", "--DEBUG", dest="DEBUG", default=False, action="store_true", help="Enable DEBUG logging")
    parser.add_argument(
        '-R',
        '--COT_RECEIVE_URL',
        dest="COT_RECEIVE_URL",
        help='URL of CoT Receiver. Must be a URL, e.g. tcp:0.0.0.0:1234 or udp:127.0.0.1:1234, etc.'
    )
    parser.add_argument(
        '-S',
        '--COT_SEND_URL',
        dest="COT_SEND_URL",
        help='URL to CoT Sender. Must be a URL, e.g. tcp:1.2.3.4:1234 or tls:...:1234, etc.'
    )
    parser.add_argument(
        "-F",
        '--FILTER_CONFIG',
        dest="FILTER_CONFIG",
        help="FILTER_CONFIG",
    )
    parser.add_argument(
        "-K",
        '--KNOWN_CRAFT',
        dest="KNOWN_CRAFT",
        help="KNOWN_CRAFT",
    )
    namespace = parser.parse_args()
    cli_args = {k: v for k, v in vars(namespace).items() if v is not None}

    # Read config file:
    config_file = cli_args.get("CONFIG_FILE")
    logging.info("Reading configuration from %s", config_file)
    config = configparser.ConfigParser()
    config.read(config_file)

    # Combined command-line args with config file:
    if "aircotproxy" in config:
        combined_config = collections.ChainMap(cli_args, os.environ, config["aircotproxy"])
    else:
        combined_config = collections.ChainMap(cli_args, os.environ)

    if combined_config.get("FILTER_CONFIG"):
        filter_config = combined_config.get("FILTER_CONFIG")
        logging.info("Reading FILTER_CONFIG from %s", filter_config)
        filters = configparser.ConfigParser()
        filters.read(filter_config)
        combined_config = collections.ChainMap(combined_config, {"FILTERS": filters})

    if not combined_config.get("COT_SEND_URL"):
        print("Please specify a CoT Sender URL, for example: '-S tcp:takserver.example.com:8087'")
        print("See -h for help.")
        sys.exit(1)

    if not combined_config.get("COT_RECEIVE_URL"):
        print("Please specify a CoT Receiver URL, for example: '-R tcp:0.0.0.0:8087'")
        print("See -h for help.")
        sys.exit(1)

    if sys.version_info[:2] >= (3, 7):
        asyncio.run(main(combined_config), debug=combined_config.get("DEBUG"))
    else:
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(main(combined_config))
        finally:
            loop.close()


if __name__ == "__main__":
    cli()
