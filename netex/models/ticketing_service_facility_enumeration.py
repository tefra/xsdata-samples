from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TicketingServiceFacilityEnumeration(Enum):
    PURCHASE = "purchase"
    COLLECTION = "collection"
    CARD_TOP_UP = "cardTopUp"
    RESERVATIONS = "reservations"
    EXCHANGE = "exchange"
    REFUND = "refund"
    RENEWAL = "renewal"
    EXCESS_FARES = "excessFares"
    OTHER = "other"
    ALL = "all"
