from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BaggageUseTypeEnumeration(StrEnum):
    CARRY_ON = "carryOn"
    CHECK_IN = "checkIn"
    OVERSIZE_CHECK_IN = "oversizeCheckIn"
    BAGGAGE_COMPARTMENT = "baggageCompartment"
