from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeTrinary(Enum):
    """
    Extension of boolean, that allows for unknown values.
    """

    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"
