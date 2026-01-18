from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SignContentEnumeration(Enum):
    ENTRANCE = "entrance"
    EXIT = "exit"
    EMERGENCY_EXIT = "emergencyExit"
    TRANSPORT_MODE = "transportMode"
    NO_SMOKING = "noSmoking"
    TICKETS = "tickets"
    ASSISTANCE = "assistance"
    SOS_PHONE = "sosPhone"
    TOUCH_POINT = "touchPoint"
    MEETING_POINT = "meetingPoint"
    TRANSPORT_MODE_POINT = "transportModePoint"
    OTHER = "other"
