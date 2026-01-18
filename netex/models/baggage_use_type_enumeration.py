from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BaggageUseTypeEnumeration(Enum):
    CARRY_ON = "carryOn"
    CHECK_IN = "checkIn"
    OVERSIZE_CHECK_IN = "oversizeCheckIn"
    BAGGAGE_COMPARTMENT = "baggageCompartment"
