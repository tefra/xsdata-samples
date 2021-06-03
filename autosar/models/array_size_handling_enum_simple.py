from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ArraySizeHandlingEnumSimple(Enum):
    """
    :cvar ALL_INDICES_DIFFERENT_ARRAY_SIZE: All elements of the variable
        size array may have different sizes.
    :cvar ALL_INDICES_SAME_ARRAY_SIZE: All elements of the variable size
        array have the same size.
    :cvar INHERITED_FROM_ARRAY_ELEMENT_TYPE_SIZE: The size of all
        dimensions of the variable size array is determined by the size
        of the contained array element.
    """
    ALL_INDICES_DIFFERENT_ARRAY_SIZE = "ALL-INDICES-DIFFERENT-ARRAY-SIZE"
    ALL_INDICES_SAME_ARRAY_SIZE = "ALL-INDICES-SAME-ARRAY-SIZE"
    INHERITED_FROM_ARRAY_ELEMENT_TYPE_SIZE = "INHERITED-FROM-ARRAY-ELEMENT-TYPE-SIZE"
