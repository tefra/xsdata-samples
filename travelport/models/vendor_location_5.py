from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_vendor_location_5 import TypeVendorLocation5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class VendorLocation5(TypeVendorLocation5):
    """
    Location definition specific to a Vendor in a specific provider (e.g. 1G)
    system.
    """

    class Meta:
        name = "VendorLocation"
        namespace = "http://www.travelport.com/schema/common_v34_0"
