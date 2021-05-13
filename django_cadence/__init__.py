#  Copyright (c) 2020 Daniel Sloan, Lucid Horizons Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

from .scheduling import cron
from django import VERSION

# Get rid of this soon. Makes deprecation warnings now in dj3.2.
if VERSION[0] == 4 or (VERSION[0] == 3 and VERSION[1] > 1):
    __all__ = ["cron"]
else:
    # Allows "legacy" style use of "django_cadence" as the app, instead of requiring the full AppConfig
    default_app_config = "django_cadence.apps.DjangoCadenceConfig"
    __all__ = ["default_app_config", "cron"]
