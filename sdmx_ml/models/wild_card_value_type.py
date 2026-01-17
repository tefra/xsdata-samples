from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


class WildCardValueType(Enum):
    """
    WildCardValueType is a single value code list, used to include the '%'
    character - indicating that an entire field is wild carded.

    :cvar PERCENT_SIGN: Indicates a wild card value.
    """

    PERCENT_SIGN = "%"
