from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFareRuleType(Enum):
    """
    The valid rule types.
    """

    NONE = "none"
    SHORT = "short"
    LONG = "long"
