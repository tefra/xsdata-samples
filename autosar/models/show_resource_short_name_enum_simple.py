from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ShowResourceShortNameEnumSimple(Enum):
    """
    :cvar NO_SHOW_SHORT_NAME: The short name of the target is '''not'''
        rendered at the place of the reference.
    :cvar SHOW_SHORT_NAME: The short name of the target is rendered at
        the place of the reference.
    """

    NO_SHOW_SHORT_NAME = "NO-SHOW-SHORT-NAME"
    SHOW_SHORT_NAME = "SHOW-SHORT-NAME"
