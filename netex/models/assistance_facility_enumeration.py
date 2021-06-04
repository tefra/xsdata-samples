from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AssistanceFacilityEnumeration(Enum):
    PERSONAL_ASSISTANCE = "personalAssistance"
    BOARDING_ASSISTANCE = "boardingAssistance"
    WHEECHAIR_ASSISTANCE = "wheechairAssistance"
    UNACCOMPANIED_MINOR_ASSISTANCE = "unaccompaniedMinorAssistance"
    WHEELCHAIR_USE = "wheelchairUse"
    CONDUCTOR = "conductor"
    INFORMATION = "information"
    OTHER = "other"
    NONE_VALUE = "none"
    ANY = "any"
