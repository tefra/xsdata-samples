from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ShowResourceLongNameEnumSimple(Enum):
    """
    :cvar NO_SHOW_LONG_NAME: The long name of the target is '''not'''
        rendered at the place of the reference.
    :cvar SHOW_LONG_NAME: The long name of the target is rendered at the
        place of the reference.
    """
    NO_SHOW_LONG_NAME = "NO-SHOW-LONG-NAME"
    SHOW_LONG_NAME = "SHOW-LONG-NAME"
