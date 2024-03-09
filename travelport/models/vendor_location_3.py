from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_vendor_location_3 import TypeVendorLocation3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class VendorLocation3(TypeVendorLocation3):
    """
    Location definition specific to a Vendor in a specific provider (e.g. 1G)
    system.
    """

    class Meta:
        name = "VendorLocation"
        namespace = "http://www.travelport.com/schema/common_v33_0"
