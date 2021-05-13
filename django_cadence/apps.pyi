from typing import Any, Callable, TypeVar, Tuple, List

from apscheduler.triggers.base import BaseTrigger

JOBS: List[Tuple[BaseTrigger, Callable[..., Any], str]]
