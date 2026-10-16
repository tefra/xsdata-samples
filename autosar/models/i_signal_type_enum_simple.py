from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ISignalTypeEnumSimple(StrEnum):
    """
    :cvar ARRAY: ISignal shall be interpreted as an array (UINT8_N,
        UINT8_DYN)
    :cvar PRIMITIVE: ISignal shall be interpreted as a primitive type
        (e.g. UINT_8, SINT_32)
    """

    ARRAY = "ARRAY"
    PRIMITIVE = "PRIMITIVE"
