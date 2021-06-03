from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticOperationCycleTypeEnumSimple(Enum):
    """
    :cvar IGNITION: Ignition ON / OFF cycle
    :cvar OBD_DRIVING_CYCLE: OBD Driving cycle
    :cvar OTHER: further operation cycle
    :cvar POWER: Power ON / OFF cycle
    :cvar TIME: Time based operation cycle
    :cvar WARMUP: OBD Warm up cycle
    """
    IGNITION = "IGNITION"
    OBD_DRIVING_CYCLE = "OBD-DRIVING-CYCLE"
    OTHER = "OTHER"
    POWER = "POWER"
    TIME = "TIME"
    WARMUP = "WARMUP"
