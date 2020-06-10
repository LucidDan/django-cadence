from typing import Optional, Callable, Union, Any
from dramatiq import Actor
from celery.app.task import Task

DecoratorInner = Union[Task, Actor, Callable[[], None]]

def cron(
    crontab: str, job_id: Optional[str] = None
) -> Callable[[DecoratorInner], DecoratorInner]: ...
