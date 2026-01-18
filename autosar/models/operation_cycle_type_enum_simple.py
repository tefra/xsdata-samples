from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class OperationCycleTypeEnumSimple(Enum):
    """
    :cvar IGNITION: Ignition ON / OFF cycle.
    :cvar OBD_DCY: OBD Driving cycle.
    :cvar OTHER: Further operation cycle.
    :cvar POWER: Power ON / OFF cycle.
    :cvar TIME: Time based operation cycle.
    :cvar WARMUP: OBD Warm up cycle.
    """

    IGNITION = "IGNITION"
    OBD_DCY = "OBD-DCY"
    OTHER = "OTHER"
    POWER = "POWER"
    TIME = "TIME"
    WARMUP = "WARMUP"
