from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class SeverityEnum(Enum):
    """
    Levels of severity of a situation as whole assessed by the impact that
    the situation may have on traffic flow as perceived by the supplier.

    :cvar HIGHEST: Perceived by supplier as being of the highest level.
    :cvar HIGH: Perceived by supplier as being of a high level.
    :cvar MEDIUM: Perceived by supplier as being of a medium level.
    :cvar LOW: Perceived by supplier as being of a low level.
    :cvar LOWEST: Perceived by supplier as being of the lowest
        discernible level.
    :cvar NONE: Perceived by supplier as having a severity rating of
        none.
    :cvar UNKNOWN: Perceived by supplier as being of an unknown level.
    """

    HIGHEST = "highest"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    LOWEST = "lowest"
    NONE = "none"
    UNKNOWN = "unknown"
