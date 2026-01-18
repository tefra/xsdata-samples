from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageServiceFacilityEnumeration(Enum):
    OTHER = "other"
    LEFT_LUGGAGE = "leftLuggage"
    PORTERAGE = "porterage"
    FREE_TROLLEYS = "freeTrolleys"
    PAID_TROLLEYS = "paidTrolleys"
    COLLECT_AND_DELIVER_TO_STATION = "collectAndDeliverToStation"
    BAGGAGE_CHECK_IN_CHECK_OUT = "baggageCheckInCheckOut"
