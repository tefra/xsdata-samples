from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypePhoneType1(StrEnum):
    """
    Specifies the phone types. (ie.

    Home, Business, Mobile, etc).
    """

    WORK = "Work"
    HOME = "Home"
    FAX = "Fax"
    MOBILE = "Mobile"
    OTHER = "Other"
