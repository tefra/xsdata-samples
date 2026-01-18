from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class RunModeSimple(Enum):
    """
    :cvar RUN_CONTINUOUS: RUN_CONTINUOUS run mode
    :cvar RUN_ONCE: RUN_ONCE run mode
    """

    RUN_CONTINUOUS = "RUN-CONTINUOUS"
    RUN_ONCE = "RUN-ONCE"
