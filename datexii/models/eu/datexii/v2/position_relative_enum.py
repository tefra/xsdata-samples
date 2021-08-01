from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PositionRelativeEnum(Enum):
    """
    Relative positions of one item to another.

    :cvar ABOVE: Positioned above relative item.
    :cvar BELOW: Positioned below relative item.
    :cvar TO_THE_LEFT: Positioned to the left of relative item.
    :cvar TO_THE_RIGHT: Positioned to the right of relative item.
    """
    ABOVE = "above"
    BELOW = "below"
    TO_THE_LEFT = "toTheLeft"
    TO_THE_RIGHT = "toTheRight"
