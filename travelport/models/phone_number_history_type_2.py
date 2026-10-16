from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class PhoneNumberHistoryType2(StrEnum):
    AGENCY = "Agency"
    BUSINESS = "Business"
    MOBILE = "Mobile"
    HOME = "Home"
    FAX = "Fax"
    HOTEL = "Hotel"
    OTHER = "Other"
    NONE = "None"
    EMAIL = "Email"
