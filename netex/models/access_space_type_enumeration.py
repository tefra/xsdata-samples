from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccessSpaceTypeEnumeration(StrEnum):
    CONCOURSE = "concourse"
    BOOKING_HALL = "bookingHall"
    FORECOURT = "forecourt"
    UNDERPASS = "underpass"
    OVERPASS = "overpass"
    PASSAGE = "passage"
    PASSAGE_SECTION = "passageSection"
    LIFT = "lift"
    GALLERY = "gallery"
    GARAGE = "garage"
    SHOP = "shop"
    WAITING_ROOM = "waitingRoom"
    RESTAURANT = "restaurant"
    OTHER = "other"
    STAIRCASE = "staircase"
    WC = "wc"
