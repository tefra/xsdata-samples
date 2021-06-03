from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EEnumSimple(Enum):
    """
    :cvar BOLD: The emphasis is preferably represented in boldface font.
    :cvar BOLDITALIC: The emphasis is preferably represented in boldface
        plus italic font.
    :cvar ITALIC: The emphasis is preferably represented in italic font.
    :cvar PLAIN: The emphasis has no specific rendering. It is used if
        e.g. semantic information is applied to the emphasis text.
    """
    BOLD = "BOLD"
    BOLDITALIC = "BOLDITALIC"
    ITALIC = "ITALIC"
    PLAIN = "PLAIN"
