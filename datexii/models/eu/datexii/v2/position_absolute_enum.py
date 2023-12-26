from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PositionAbsoluteEnum(Enum):
    """
    Absolute positions of an item within an alloted space.

    :cvar ON_LEFT: On the left of the allotted space.
    :cvar ON_RIGHT: On the right of the allotted space.
    :cvar AT_TOP: At the top of the allotted space.
    :cvar AT_BOTTOM: At the bottom of the allotted space.
    """

    ON_LEFT = "onLeft"
    ON_RIGHT = "onRight"
    AT_TOP = "atTop"
    AT_BOTTOM = "atBottom"
