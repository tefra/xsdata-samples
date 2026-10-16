from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ReservedSpaceFacilityEnumeration(StrEnum):
    UNKNOWN = "unknown"
    LOUNGE = "lounge"
    HALL = "hall"
    MEETING_POINT = "meetingPoint"
    GROUP_POINT = "groupPoint"
    RECEPTION = "reception"
    SHELTER = "shelter"
    SEATS = "seats"
