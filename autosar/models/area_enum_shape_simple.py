from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class AreaEnumShapeSimple(Enum):
    """
    :cvar CIRCLE: The shape is a circle.
    :cvar DEFAULT: This specifies the fact that the area covers the rest
        of the figure.
    :cvar POLY: The area is specified as polygon.
    :cvar RECT: The shape is specified as rectangle.
    """

    CIRCLE = "CIRCLE"
    DEFAULT = "DEFAULT"
    POLY = "POLY"
    RECT = "RECT"
