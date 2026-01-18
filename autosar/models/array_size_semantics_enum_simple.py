from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ArraySizeSemanticsEnumSimple(Enum):
    """
    :cvar FIXED_SIZE: This means that the ApplicationArrayDataType will
        always have a fixed number of elements.
    :cvar VARIABLE_SIZE: This implies that the actual number of elements
        in the ApplicationArrayDataType might vary at run-time. The
        value of arraySize represents the maximum number of elements in
        the array.
    """

    FIXED_SIZE = "FIXED-SIZE"
    VARIABLE_SIZE = "VARIABLE-SIZE"
