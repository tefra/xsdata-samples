from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class PhoneNumberHistoryType1(StrEnum):
    AGENCY = "Agency"
    BUSINESS = "Business"
    MOBILE = "Mobile"
    HOME = "Home"
    FAX = "Fax"
    HOTEL = "Hotel"
    OTHER = "Other"
    NONE = "None"
    EMAIL = "Email"
