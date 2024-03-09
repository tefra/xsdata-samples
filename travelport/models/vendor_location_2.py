from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_vendor_location_2 import TypeVendorLocation2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class VendorLocation2(TypeVendorLocation2):
    """
    Location definition specific to a Vendor in a specific provider (e.g. 1G)
    system.
    """

    class Meta:
        name = "VendorLocation"
        namespace = "http://www.travelport.com/schema/common_v32_0"
