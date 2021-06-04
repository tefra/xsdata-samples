from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UsageEndEnumeration(Enum):
    STANDARD_DURATION = "standardDuration"
    END_OF_CALENDAR_PERIOD = "endOfCalendarPeriod"
    END_OF_RIDE = "endOfRide"
    END_OF_TRIP = "endOfTrip"
    END_OF_FARE_DAY = "endOfFareDay"
    END_OF_FARE_PERIOD = "endOfFarePeriod"
    PRODUCT_EXPIRY = "productExpiry"
    PROFILE_EXPIRY = "profileExpiry"
    DEREGISTRATION = "deregistration"
    OTHER = "other"
