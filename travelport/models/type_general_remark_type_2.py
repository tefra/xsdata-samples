from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeGeneralRemarkType2(StrEnum):
    """
    A code for categorizing a remark within the GDS.
    """

    ALPHA = "Alpha"
    BASIC = "Basic"
    HISTORICAL = "Historical"
    INVOICE = "Invoice"
    ITINERARY = "Itinerary"
    VENDOR = "Vendor"
