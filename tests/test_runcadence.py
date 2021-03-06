"""
tests.test_runcadence

Test the runcadence management command that starts the main scheduler loop.
"""

#  Copyright (c) 2020 Daniel Sloan, Lucid Horizons Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
from io import StringIO
from typing import TYPE_CHECKING

from django.core.management import call_command

if TYPE_CHECKING:
    from unittest.mock import MagicMock


def test_run_management_command(settings, mocker):
    from django_cadence import dispatcher

    out = StringIO()

    dispatcher_obj: "MagicMock" = mocker.patch.object(
        dispatcher, "start_dispatcher", autospec=True
    )

    call_command("runcadence", stdout=out)

    dispatcher_obj.assert_called_once()
