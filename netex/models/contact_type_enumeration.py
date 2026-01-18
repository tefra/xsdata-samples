from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ContactTypeEnumeration(Enum):
    ANY = "any"
    INFORMATION = "information"
    RESERVATIONS = "reservations"
    LOST_PROPERTY = "lostProperty"
    PUBLIC_RELATIONS = "publicRelations"
    COMPLAINTS = "complaints"
    EMERGENCY = "emergency"
    OTHER = "other"
