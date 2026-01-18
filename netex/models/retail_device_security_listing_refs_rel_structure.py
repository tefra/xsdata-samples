from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .retail_device_security_listing_ref import RetailDeviceSecurityListingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDeviceSecurityListingRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "RetailDeviceSecurityListingRefs_RelStructure"

    retail_device_security_listing_ref: Iterable[
        RetailDeviceSecurityListingRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
