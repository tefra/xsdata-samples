from __future__ import annotations

from dataclasses import dataclass, field

from .retail_device_ref import RetailDeviceRef
from .security_listing_versioned_child_structure import (
    SecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailDeviceSecurityListingVersionedChildStructure(
    SecurityListingVersionedChildStructure
):
    class Meta:
        name = "RetailDeviceSecurityListing_VersionedChildStructure"

    retail_device_ref: None | RetailDeviceRef = field(
        default=None,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
