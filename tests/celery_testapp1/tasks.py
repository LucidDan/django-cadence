#  Copyright (c) 2020 Daniel Sloan, Lucid Horizons Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

import time

from celery import shared_task
from django_cadence import cron


def i_was_called():
    """No-op function that can be mocked for testing purposes"""
    pass


@cron("0 0 * * *")
@shared_task
def sometask():
    print("Task executed")
    i_was_called()
