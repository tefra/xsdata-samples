from dataclasses import dataclass

from .retail_device_security_listing_ref_structure import (
    RetailDeviceSecurityListingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailDeviceSecurityListingRef(RetailDeviceSecurityListingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
