from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class FrameEnumSimple(Enum):
    """
    :cvar ALL: Borders all around the table
    :cvar BOTTOM: Border at the bottom of the table
    :cvar NONE: No borders around the table
    :cvar SIDES: Borders at the sides of the table
    :cvar TOP: Border at the top of the table
    :cvar TOPBOT: Borders at the top and bottom of  the table
    """
    ALL = "ALL"
    BOTTOM = "BOTTOM"
    NONE = "NONE"
    SIDES = "SIDES"
    TOP = "TOP"
    TOPBOT = "TOPBOT"
