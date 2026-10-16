from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RegisterBreakOfJourneyEnumeration(StrEnum):
    NONE = "none"
    MARK_BY_STAFF = "markByStaff"
    MARK_BY_VALIDATOR = "markByValidator"
    MARK_BY_MOBILE_APP = "markByMobileApp"
    OTHER = "other"
