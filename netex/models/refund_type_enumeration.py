from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RefundTypeEnumeration(StrEnum):
    UNUSED = "unused"
    DELAY = "delay"
    CANCELLATION = "cancellation"
    PARTIAL_JOURNEY = "partialJourney"
    EARLY_TERMINATION = "earlyTermination"
    CHANGE_OF_GROUP_SIZE = "changeOfGroupSize"
    OTHER = "other"
