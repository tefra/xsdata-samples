from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DtcFormatTypeEnumSimple(Enum):
    """
    :cvar J_1939: Defines the J1939 DTC format.
    :cvar OBD: Defines the OBD DTC format.
    :cvar UDS: Defines the UDS DTC format.
    """

    J_1939 = "J-1939"
    OBD = "OBD"
    UDS = "UDS"
