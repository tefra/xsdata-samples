from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ContactTypeEnumeration(StrEnum):
    ANY = "any"
    INFORMATION = "information"
    RESERVATIONS = "reservations"
    LOST_PROPERTY = "lostProperty"
    PUBLIC_RELATIONS = "publicRelations"
    COMPLAINTS = "complaints"
    EMERGENCY = "emergency"
    OTHER = "other"
