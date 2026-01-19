from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"


class WildCardValueType(Enum):
    """
    WildCardValueType is a single value code list, used to include the '%'
    character - indicating that an entire field is wildcarded.

    :cvar PERCENT_SIGN: Indicates a wild card value.
    """

    PERCENT_SIGN = "%"
