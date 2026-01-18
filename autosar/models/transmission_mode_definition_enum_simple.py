from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TransmissionModeDefinitionEnumSimple(Enum):
    """
    :cvar CYCLIC: The data is assumed to be transmitted in a cyclic
        manner. The cycle is defined by dataUpdatePeriod.
    :cvar CYCLIC_AND_ON_CHANGE: The data is assumed to be transmitted in
        a cyclic manner (with cycle time dataUpdatePeriod) and
        additionally there may be arbitrary transmission if the data
        value changes (minimumSendInterval to be respected, if defined).
    :cvar TRIGGERED: The data is assumed to be transmitted in an
        arbitrary manner (minimumSendInterval to be respected, if
        defined).
    """

    CYCLIC = "CYCLIC"
    CYCLIC_AND_ON_CHANGE = "CYCLIC-AND-ON-CHANGE"
    TRIGGERED = "TRIGGERED"
