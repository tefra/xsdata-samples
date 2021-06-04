from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.quay_ref import QuayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QuayRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "quayRefs_RelStructure"

    quay_ref: List[QuayRef] = field(
        default_factory=list,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
