from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


class TypeFarePull6(StrEnum):
    REVERSE_OF_ORIGIN_DESTINATION = "ReverseOfOriginDestination"
    SAME_AS_ORIGIN_DESTINATION = "SameAsOriginDestination"
