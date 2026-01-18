from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticConnectedIndicatorBehaviorEnumSimple(Enum):
    """
    :cvar BLINK_MODE: The indicator blinks when the event has status
        FAILED.
    :cvar BLINK_OR_CONTINUOUS_ON_MODE: The indicator is active and
        blinks when the event has status FAILED.
    :cvar CONTINUOUS_ON_MODE: The indicator is active when the event has
        status FAILED.
    :cvar FAST_FLASHING_MODE: Flash Indicator Lamp should be set to
        "Fast Flash".
    :cvar SLOW_FLASHING_MODE: Flash Indicator Lamp should be set to
        "Slow Flash".
    """

    BLINK_MODE = "BLINK-MODE"
    BLINK_OR_CONTINUOUS_ON_MODE = "BLINK-OR-CONTINUOUS-ON-MODE"
    CONTINUOUS_ON_MODE = "CONTINUOUS-ON-MODE"
    FAST_FLASHING_MODE = "FAST-FLASHING-MODE"
    SLOW_FLASHING_MODE = "SLOW-FLASHING-MODE"
