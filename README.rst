aircotproxy - AIS Cursor-on-Target Gateway.
****************************************
**IF YOU HAVE AN URGENT OPERATIONAL NEED**: Email ops@undef.net or call/sms +1-415-598-8226

.. image:: docs/screenshot-1601068921-25.png
   :alt: Screenshot of AIS points in ATAK-Div Developer Edition.
   :target: docs/screenshot-1601068921.png


aircotproxy receives AIS Sentences from an AIS Receiver, such as ais-decoder,
converts them to Cursor-on-Target Events, and transmits the CoT Events to a destination.

For use with CoT systems such as ATAK, WinTAK, etc. See https://www.civtak.org/ for more information on the TAK
program.

Utilized for an open ocean boat race in the Northern Pacific Ocean, as
described in this article: http://ampledata.org/boat_race_support.html

Support AISCoT Development
==========================

AISCoT has been developed for the Disaster Response, Public Safety and Frontline community at-large. This software
is currently provided at no-cost to our end-users. All development is self-funded and all time-spent is entirely
voluntary. Any contribution you can make to further these software development efforts, and the mission of AISCoT
to provide ongoing SA capabilities to our end-users, is greatly appreciated:

.. image:: https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png
    :target: https://www.buymeacoffee.com/ampledata
    :alt: Support AISCoT development: Buy me a coffee!

Installation
============


The AIS to Cursor on Target Gateway is provided by a command-line tool
called `aircotproxy`, which can be installed several ways.

Installing as a Debian/Ubuntu Package::

    $ wget https://github.com/ampledata/pytak/releases/latest/download/python3-pytak_latest_all.deb
    $ sudo apt install -f ./python3-pytak_latest_all.deb
    $ wget https://github.com/ampledata/aircotproxy/releases/latest/download/python3-aircotproxy_latest_all.deb
    $ sudo apt install -f ./python3-aircotproxy_latest_all.deb

Install from the Python Package Index::

    $ pip install aircotproxy


Install from this source tree::

    $ git clone https://github.com/ampledata/aircotproxy.git
    $ cd aircotproxy/
    $ python setup.py aircotproxy


Usage
=====

The `aircotproxy` daemon has several runtime arguments::

    $ aircotproxy -h
    usage: aircotproxy [-h] [-c CONFIG_FILE] [-d] [-U COT_URL] [-P AIS_PORT] [-S COT_STALE] [-F FILTER_CONFIG] [-K KNOWN_CRAFT]

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG_FILE, --CONFIG_FILE CONFIG_FILE
      -d, --DEBUG           Enable DEBUG logging
      -U COT_URL, --COT_URL COT_URL
                            URL to CoT Destination. Must be a URL, e.g. tcp:1.2.3.4:1234 or tls:...:1234, etc.
      -P AIS_PORT, --AIS_PORT AIS_PORT
                            AIS UDP Listen Port.
      -S COT_STALE, --COT_STALE COT_STALE
                            CoT Stale period, in seconds
      -F FILTER_CONFIG, --FILTER_CONFIG FILTER_CONFIG
                            FILTER_CONFIG
      -K KNOWN_CRAFT, --KNOWN_CRAFT KNOWN_CRAFT
                            KNOWN_CRAFT

See example-config.ini for example configuration.

Source
======
Github: https://github.com/ampledata/aircotproxy

Author
======
Greg Albrecht W2GMD oss@undef.net

http://ampledata.org/

Copyright
=========

* aircotproxy Copyright 2021 Orion Labs, Inc.
* pyAISm.py Copyright 2016 Pierre Payen

License
=======

* aircotproxy is licensed under the Apache License, Version 2.0. See LICENSE for details.
* pyAISm.py is licensed under the MIT License. See aircotproxy/pyAISm.py for details.
