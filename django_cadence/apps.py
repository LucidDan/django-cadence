"""
apps.py

The AppConfig for the django-cadence app, which provides initialization
of the known job list.
"""

#  Copyright (c) 2020 Daniel Sloan, Lucid Horizons Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

import logging
from importlib import import_module

from django.apps import AppConfig
from django.apps import apps

logger = logging.getLogger(__name__)
JOBS = []


class DjangoCadenceConfig(AppConfig):
    name = "django_cadence"
    loaded = False

    def ready(self):
        if not self.loaded:
            self.loaded = True

            # For each app in INSTALLED_APPS, make sure we import the tasks module, so that any cron tasks are found.
            for app_config in apps.get_app_configs():
                try:
                    mod = import_module(f"{app_config.name}.tasks")
                    logger.info("Loaded module %s.tasks: %s", app_config.name, mod)
                except ModuleNotFoundError:
                    logger.debug("No tasks module in %s", app_config.name)
                except ImportError:
                    logger.error("Error loading {app_config.name}.tasks", exc_info=True)
