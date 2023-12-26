from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeRemarkType1(Enum):
    """A code for categorizing a remark.

    This may include General Remarks, Itinerary Remarks, Accounting
    Remark, Name Remark, etc.
    """

    GENERAL = "General"
    ITINERARY = "Itinerary"
    ACCOUNTING = "Accounting"
    NAME = "Name"
    INTERNAL_ONLY = "Internal Only"
    HIGHLY_SENSITIVE = "Highly Sensitive"
    OSI = "OSI"
