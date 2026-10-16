from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccessFacilityEnumeration(StrEnum):
    UNKNOWN = "unknown"
    LIFT = "lift"
    WHEELCHAIR_LIFT = "wheelchairLift"
    ESCALATOR = "escalator"
    TRAVELATOR = "travelator"
    RAMP = "ramp"
    AUTOMATIC_RAMP = "automaticRamp"
    STEPS = "steps"
    STAIRS = "stairs"
    SLIDING_STEP = "slidingStep"
    SHUTTLE = "shuttle"
    NARROW_ENTRANCE = "narrowEntrance"
    BARRIER = "barrier"
    LOW_FLOOR_ACCESS = "lowFloorAccess"
    VALIDATOR = "validator"
