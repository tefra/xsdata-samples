from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_vendor_location_4 import TypeVendorLocation4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class VendorLocation4(TypeVendorLocation4):
    """
    Location definition specific to a Vendor in a specific provider (e.g.
    1G) system.
    """

    class Meta:
        name = "VendorLocation"
        namespace = "http://www.travelport.com/schema/common_v37_0"
