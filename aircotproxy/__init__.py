#!/usr/bin/env python
# -*- coding: utf-8 -*-

# AirCoTProxy - CoT to CoT Proxy Gateway with known craft lookups.

"""
AirCoTProxy - CoT to CoT Proxy Gateway with known craft lookups.
~~~~


:author: Greg Albrecht W2GMD <oss@undef.net>
:copyright: Copyright 2021 Orion Labs, Inc.
:license: Apache License, Version 2.0
:source: <https://github.com/ampledata/aircotproxy>

"""

from .constants import LOG_FORMAT, LOG_LEVEL  # NOQA

from .functions import cot_to_cot  # NOQA

from .classes import ACPWorker  # NOQA

__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"
