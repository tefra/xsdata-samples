from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ComparisonOperatorEnum(Enum):
    """
    Logical comparison operations.

    :cvar EQUAL_TO: Logical comparison operator of "equal to".
    :cvar GREATER_THAN: Logical comparison operator of "greater than".
    :cvar GREATER_THAN_OR_EQUAL_TO: Logical comparison operator of
        "greater than or equal to".
    :cvar LESS_THAN: Logical comparison operator of "less than".
    :cvar LESS_THAN_OR_EQUAL_TO: Logical comparison operator of "less
        than or equal to".
    """

    EQUAL_TO = "equalTo"
    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL_TO = "greaterThanOrEqualTo"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL_TO = "lessThanOrEqualTo"
