from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .retail_device_ref import RetailDeviceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailDeviceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "retailDeviceRefs_RelStructure"

    retail_device_ref: List[RetailDeviceRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )