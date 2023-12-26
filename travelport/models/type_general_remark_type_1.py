from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeGeneralRemarkType1(Enum):
    """
    A code for categorizing a remark within the GDS.
    """

    ALPHA = "Alpha"
    BASIC = "Basic"
    HISTORICAL = "Historical"
    INVOICE = "Invoice"
    ITINERARY = "Itinerary"
    VENDOR = "Vendor"
