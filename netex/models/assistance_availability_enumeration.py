from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AssistanceAvailabilityEnumeration(StrEnum):
    NONE = "none"
    AVAILABLE = "available"
    AVAILABLE_IF_BOOKED = "availableIfBooked"
    AVAILABLE_AT_CERTAIN_TIMES = "availableAtCertainTimes"
    AVAILABLE_DEPENDENT_ON_JOURNEY = "availableDependentOnJourney"
    UNKNOWN = "unknown"
