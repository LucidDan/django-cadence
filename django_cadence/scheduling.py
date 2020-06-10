"""
scheduling.py

Decorators to wrap django functions and make them scheduled.

"""

# Copyright (c) 2020 Daniel Sloan, Lucid Horizons Pty Ltd

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Callable, Union, Optional, TYPE_CHECKING

from apscheduler.triggers.cron import CronTrigger

from .apps import JOBS


def cron(crontab, job_id=None):
    """
    Wrap a regular function, Celery task, or Dramatiq actor in a cron schedule.
    """
    trigger = CronTrigger.from_crontab(crontab)

    def decorator(f):
        """Create a scheduled trigger for the decorated callable"""

        # We might be getting called as a wrapper of a regular callable (function, class, etc)
        # Or we might be getting called as a wrapper of a Dramatiq or Celery task.
        # We'll start out just adding the callable to the JOBS list, but for example Dramatiq
        # actors should be invoked as "<f>.send()", and Celery tasks should be invoked as
        # "<f>.apply_async()".

        if hasattr(f, "send"):
            # It's (probably) a Dramatiq Actor
            func_call = f.send
            job_name = job_id or f"{f.fn.__module__}.{f.fn.__name__}"
        elif hasattr(f, "apply_async"):
            # It's a Celery task or shared_task
            func_call = f.apply_async
            job_name = job_id or f"{f.name}"
        else:
            # It's something else, probably just a regular callable - call it directly and use repr() as the name
            func_call = f
            job_name = job_id or f"{f.__module__}.{f.__name__}"
        JOBS.append((trigger, func_call, job_name))
        return f

    return decorator
