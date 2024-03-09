from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


class TypeRailSegmentInfo(Enum):
    """
    Extra for ExtraSegmentInfo and Vendor for VendorMessages.
    """

    EXTRA = "Extra"
    VENDOR = "Vendor"
    SERVICES = "Services"
