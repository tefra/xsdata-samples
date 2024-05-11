from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AssistanceAvailabilityEnumeration(Enum):
    NONE = "none"
    AVAILABLE = "available"
    AVAILABLE_IF_BOOKED = "availableIfBooked"
    AVAILABLE_AT_CERTAIN_TIMES = "availableAtCertainTimes"
    AVAILABLE_DEPENDENT_ON_JOURNEY = "availableDependentOnJourney"
    UNKNOWN = "unknown"
