from typing import Any, Callable, Type, Tuple, List

from apscheduler.triggers.base import BaseTrigger

JOBS: List[Tuple[Type[BaseTrigger], Callable[..., Any], str]]
