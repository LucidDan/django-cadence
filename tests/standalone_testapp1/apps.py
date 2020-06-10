"""
tests.standalone_testapp1.apps

Test app used by test cases. Works in a standalone manner to add some tasks.
"""

#  Copyright (c) 2020 Daniel Sloan, Lucid Horizons Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class StandaloneTestApp1Config(AppConfig):
    name = "standalone_testapp1"
    loaded = False

    def ready(self):
        if not self.loaded:
            self.loaded = True
