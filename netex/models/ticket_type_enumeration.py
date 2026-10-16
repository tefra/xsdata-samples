from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TicketTypeEnumeration(StrEnum):
    STANDARD = "standard"
    PROMOTION = "promotion"
    CONCESSION = "concession"
    GROUP = "group"
    SEASON = "season"
    CARNET = "carnet"
    TRAVEL_CARD = "travelCard"
    OTHER = "other"
    ALL = "all"
