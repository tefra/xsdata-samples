from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SuspensionPolicyEnumeration(StrEnum):
    NONE = "none"
    FOR_CERTIFIED_ILLNESS = "forCertifiedIllness"
    FOR_PARENTAL_LEAVE = "forParentalLeave"
    FOR_HOLIDAY = "forHoliday"
    FOR_ANY_REASON = "forAnyReason"
