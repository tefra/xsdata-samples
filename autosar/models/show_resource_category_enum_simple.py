from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ShowResourceCategoryEnumSimple(Enum):
    """
    :cvar NO_SHOW_CATEGORY: The category of the target is '''not'''
        rendered at the place of the reference.
    :cvar SHOW_CATEGORY: The category of the target is  rendered at the
        place of the reference.
    """

    NO_SHOW_CATEGORY = "NO-SHOW-CATEGORY"
    SHOW_CATEGORY = "SHOW-CATEGORY"
