from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TimeBaseResourceSubtypesEnum(StrEnum):
    SYNCHRONIZED_TIME_BASE_CONSUMER = "SYNCHRONIZED-TIME-BASE-CONSUMER"
    SYNCHRONIZED_TIME_BASE_PROVIDER = "SYNCHRONIZED-TIME-BASE-PROVIDER"
    TIME_BASE_RESOURCE = "TIME-BASE-RESOURCE"
