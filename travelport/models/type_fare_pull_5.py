from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


class TypeFarePull5(StrEnum):
    REVERSE_OF_ORIGIN_DESTINATION = "ReverseOfOriginDestination"
    SAME_AS_ORIGIN_DESTINATION = "SameAsOriginDestination"
