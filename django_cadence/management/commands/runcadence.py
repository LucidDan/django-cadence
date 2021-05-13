"""
runcadence.py

Management command to run the main scheduler loop. This runs in a separate process
and is responsible for making sure scheduled tasks are executed at the right time.

Typically, it is running in an environment with Dramatiq or Celery, and mostly just
 dispatches tasks to the worker processes. However it might also run standalone,
 in which case it will dispatch the tasks to its own pool of multiprocessing workers.
"""

#  Copyright (c) 2020 Daniel Sloan, Lucid Horizons Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

import multiprocessing

from django.core.management.base import BaseCommand
from django_cadence.dispatcher import start_dispatcher

CPU_COUNT = multiprocessing.cpu_count()


class Command(BaseCommand):
    help = "Runs Cadence scheduled tasks."

    def add_arguments(self, parser):
        parser.add_argument(
            "--processes",
            "-p",
            default=CPU_COUNT,
            type=int,
            help="The number of processes to run (default: %d)." % CPU_COUNT,
        )

    def handle(self, processes, **options):
        """Handle a call to the command via manage.py"""

        # Note: if we're using dramatiq (and maybe celery), we should not have multiple processes
        if processes > 1:
            self.stdout.write(
                "WARNING: Multi-process mode for dramatiq or celery is not recommended due to potential pickling issues."
            )
            self.stdout.flush()
        # Set up and run the job dispatcher
        start_dispatcher(processes=processes)
