from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleAccessFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    WHEELCHAIR_LIFT = "wheelchairLift"
    MANUAL_RAMP = "manualRamp"
    AUTOMATIC_RAMP = "automaticRamp"
    STEPS = "steps"
    SLIDING_STEP = "slidingStep"
    NARROW_ENTRANCE = "narrowEntrance"
    VALIDATOR = "validator"
