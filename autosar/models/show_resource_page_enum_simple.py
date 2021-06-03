from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ShowResourcePageEnumSimple(Enum):
    """
    :cvar NO_SHOW_PAGE: The page number  of the target is '''not'''
        rendered at the place of the reference.
    :cvar SHOW_PAGE: The page number  of the target is rendered at the
        place of the reference.
    """
    NO_SHOW_PAGE = "NO-SHOW-PAGE"
    SHOW_PAGE = "SHOW-PAGE"
