from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccommodationAccessEnumeration(StrEnum):
    OTHER = "other"
    FREE_SEATING = "freeSeating"
    RESERVATION = "reservation"
    STANDING = "standing"
