from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_vendor_location_1 import TypeVendorLocation1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class VendorLocation1(TypeVendorLocation1):
    """
    Location definition specific to a Vendor in a specific provider (e.g. 1G)
    system.
    """
    class Meta:
        name = "VendorLocation"
        namespace = "http://www.travelport.com/schema/common_v52_0"
