from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeTrinary(StrEnum):
    """
    Extension of boolean, that allows for unknown values.
    """

    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"
