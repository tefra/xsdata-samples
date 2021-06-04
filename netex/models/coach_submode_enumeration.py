from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CoachSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    INTERNATIONAL_COACH = "internationalCoach"
    NATIONAL_COACH = "nationalCoach"
    SHUTTLE_COACH = "shuttleCoach"
    REGIONAL_COACH = "regionalCoach"
    SPECIAL_COACH = "specialCoach"
    SCHOOL_COACH = "schoolCoach"
    SIGHTSEEING_COACH = "sightseeingCoach"
    TOURIST_COACH = "touristCoach"
    COMMUTER_COACH = "commuterCoach"
