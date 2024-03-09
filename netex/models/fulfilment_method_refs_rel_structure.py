from dataclasses import dataclass, field
from typing import List

from .fulfilment_method_ref import FulfilmentMethodRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FulfilmentMethodRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "fulfilmentMethodRefs_RelStructure"

    fulfilment_method_ref: List[FulfilmentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
