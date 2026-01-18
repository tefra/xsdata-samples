from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ScaleConstrValidityEnumSimple(Enum):
    """
    :cvar NOT_AVAILABLE: Currently invalid area The value usually is
        presented by the ECU but can currently not be performed due to
        e.g. initialization or temporary problems. Please note, that
        this behavior appears during runtime and cannot be handled while
        data is edited.
    :cvar NOT_DEFINED: Indicates an area which is marked in a
        specification (e.g. as reserved) Shall usually not be set by the
        ECU but is used by a tester to verify correct ECU.
    :cvar NOT_VALID: The ECU cannot process the requested data.
    :cvar VALID: Current value is within a valid range and can be
        presented to user as is.
    """

    NOT_AVAILABLE = "NOT-AVAILABLE"
    NOT_DEFINED = "NOT-DEFINED"
    NOT_VALID = "NOT-VALID"
    VALID = "VALID"
