"""
dispatcher.py

The dispatcher loop that handles processing scheduled events and dispatching
tasks either to a task framework (e.g. Dramatiq or Celery) or to a pool of
sub-processes.
"""

#  Copyright (c) 2020 Daniel Sloan, Lucid Horizons Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

import logging
import signal

from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from pytz import utc

from django_cadence.apps import JOBS

logger = logging.getLogger(__name__)


def start_dispatcher(processes):
    """Start the dispatcher loop"""

    logger.info("Starting job dispatcher loop")
    # FIXME: Get timezone from django ?
    tz = utc
    jobstores = {
        "default": MemoryJobStore(),
        # FIXME: Add support for using Django model as job store in future
        # 'django': DjangoJobStore()
    }
    # Note: we can't pickle dramatiq actors, so doing this in multi-process is a bad idea.
    #  Haven't come up with a great solution to this yet, but it'll probably be something along
    #  the lines of storing caller type information and just pickle the function, not the function.send
    if processes > 1:
        # Process pool; good for cases where we are not using Celery or Dramatiq and need to start a process for each
        #  task to be handled in this process.
        executors = {
            "default": ProcessPoolExecutor(max_workers=processes),
        }
    else:
        # Thread pool; for very small thread-safe environments or where all we do is send tasks to Celery or Dramatiq
        executors = {"default": ThreadPoolExecutor(max_workers=8)}

    scheduler = BlockingScheduler(
        logger=logger, timezone=tz, executors=executors, jobstores=jobstores
    )

    for trigger, func, job_id in JOBS:
        logger.debug("Adding task: %s - schedule %r", job_id, trigger)
        scheduler.add_job(
            func,
            trigger=trigger,
            name=job_id,
            id=job_id,
            max_instances=1,
            replace_existing=True,
        )

    def shutdown(signum, frame):
        scheduler.shutdown()

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    logger.debug("Starting blocking main loop for cron server...")
    scheduler.start()
    logger.debug("Shutting down main loop")
