from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class AlignEnumSimple(Enum):
    """
    :cvar CENTER: The content of the table is horizontally centered.
    :cvar JUSTIFY: This indicates that the content of table cell shall
        be justified (rendered as a block where white-space is expanded
        such that all lines are filled up).
    :cvar LEFT: This indicates that the content of a table cell is left
        justified.
    :cvar RIGHT: This indicates that the content of a table cell is left
        justified.
    """

    CENTER = "CENTER"
    JUSTIFY = "JUSTIFY"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
