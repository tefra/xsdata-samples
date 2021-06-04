from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SuspensionPolicyEnumeration(Enum):
    NONE_VALUE = "none"
    FOR_CERTIFIED_ILLNESS = "forCertifiedIllness"
    FOR_PARENTAL_LEAVE = "forParentalLeave"
    FOR_HOLIDAY = "forHoliday"
    FOR_ANY_REASON = "forAnyReason"
