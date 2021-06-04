from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.retail_device_security_listing_ref import RetailDeviceSecurityListingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailDeviceSecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "RetailDeviceSecurityListingRefs_RelStructure"

    retail_device_security_listing_ref: List[RetailDeviceSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
