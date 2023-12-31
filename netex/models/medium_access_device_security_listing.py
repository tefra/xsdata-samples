from dataclasses import dataclass
from .medium_access_device_security_listing_versioned_child_structure import (
    MediumAccessDeviceSecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MediumAccessDeviceSecurityListing(
    MediumAccessDeviceSecurityListingVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
