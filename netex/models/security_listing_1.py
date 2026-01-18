from __future__ import annotations

from dataclasses import dataclass

from .security_listing_versioned_child_structure import (
    SecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SecurityListing1(SecurityListingVersionedChildStructure):
    class Meta:
        name = "SecurityListing"
        namespace = "http://www.netex.org.uk/netex"
