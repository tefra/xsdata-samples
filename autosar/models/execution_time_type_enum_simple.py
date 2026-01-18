from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ExecutionTimeTypeEnumSimple(Enum):
    """
    :cvar GROSS: Indicates that the given execution time is the time
        used to execute the ExecutableEntity without any interruption
        and and including external calls.
    :cvar NET: Indicates that the given execution time is the time used
        to execute the ExecutableEntity without any interruption and
        without any external calls.
    """

    GROSS = "GROSS"
    NET = "NET"
