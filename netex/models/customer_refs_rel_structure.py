from dataclasses import dataclass, field
from typing import List
from netex.models.customer_ref import CustomerRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerRefs_RelStructure"

    customer_ref: List[CustomerRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
