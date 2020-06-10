#  Copyright (c) 2020 Daniel Sloan, Lucid Horizons Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#


def test_discover_events(settings, mocker):
    from django_cadence.apps import JOBS

    job_names = set(map(lambda x: x[2], JOBS))

    assert "tests.standalone_testapp1.tasks.sometask" in job_names
    assert "tests.dramatiq_testapp1.tasks.sometask" in job_names
    assert "tests.celery_testapp1.tasks.sometask" in job_names
