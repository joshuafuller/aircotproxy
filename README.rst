aircotproxy - CoT Event Transform Proxy.
****************************************
**IF YOU HAVE AN URGENT OPERATIONAL NEED**: Email ops@undef.net or call/sms +1-415-598-8226

AirCotProxy transforms received CoT Events based on a Known Craft database (CSV). Event Type, Name,
and Callsign can all be specified with the Known Craft database.

For use with CoT systems such as ATAK, WinTAK, etc. See https://www.civtak.org/ for more information on the TAK
program.

Support AirCotProxy Development
===============================

AirCotProxy has been developed for the Disaster Response, Public Safety and Frontline community at-large. This software
is currently provided at no-cost to our end-users. All development is self-funded and all time-spent is entirely
voluntary. Any contribution you can make to further these software development efforts, and the mission of AirCotProxy
to provide ongoing SA capabilities to our end-users, is greatly appreciated:

.. image:: https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png
    :target: https://www.buymeacoffee.com/ampledata
    :alt: Support AirCotProxy development: Buy me a coffee!

Installation
============

AirCotProxy is provided by a command-line tool
called `aircotproxy`, which can be installed several ways.

Installing as a Debian/Ubuntu Package::

    $ wget https://github.com/ampledata/pytak/releases/latest/download/python3-pytak_latest_all.deb
    $ sudo apt install -f ./python3-pytak_latest_all.deb
    $ wget https://github.com/ampledata/aircot/releases/latest/download/python3-aircot_latest_all.deb
    $ sudo apt install -f ./python3-aircot_latest_all.deb
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
    usage: aircotproxy [-h] [-c CONFIG_FILE] [-d] [-R COT_RECEIVE_URL] [-S COT_SEND_URL] [-F FILTER_CONFIG] [-K KNOWN_CRAFT]

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG_FILE, --CONFIG_FILE CONFIG_FILE
      -d, --DEBUG           Enable DEBUG logging
      -R COT_RECEIVE_URL, --COT_RECEIVE_URL COT_RECEIVE_URL
                            URL of CoT Receiver. Must be a URL, e.g. tcp:0.0.0.0:1234 or udp:127.0.0.1:1234, etc.
      -S COT_SEND_URL, --COT_SEND_URL COT_SEND_URL
                            URL to CoT Sender. Must be a URL, e.g. tcp:1.2.3.4:1234 or tls:...:1234, etc.
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

License
=======

* aircotproxy is licensed under the Apache License, Version 2.0. See LICENSE for details.
