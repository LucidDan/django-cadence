from typing import Any, Callable, TypeVar, Tuple, List

from apscheduler.triggers.base import BaseTrigger

TriggerType = TypeVar("TriggerType", bound=BaseTrigger)
JOBS: List[Tuple[TriggerType, Callable[..., Any], str]]
