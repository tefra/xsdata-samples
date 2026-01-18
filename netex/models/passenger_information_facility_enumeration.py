from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PassengerInformationFacilityEnumeration(Enum):
    NEXT_STOP_INDICATOR = "nextStopIndicator"
    STOP_ANNOUNCEMENTS = "stopAnnouncements"
    PASSENGER_INFORMATION_DISPLAY = "passengerInformationDisplay"
    REAL_TIME_CONNECTIONS = "realTimeConnections"
    OTHER = "other"
