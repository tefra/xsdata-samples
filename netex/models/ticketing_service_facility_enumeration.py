from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TicketingServiceFacilityEnumeration(StrEnum):
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
