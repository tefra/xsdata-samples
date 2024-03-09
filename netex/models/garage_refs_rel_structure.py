from dataclasses import dataclass, field
from typing import List

from .garage_ref import GarageRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GarageRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "garageRefs_RelStructure"

    garage_ref: List[GarageRef] = field(
        default_factory=list,
        metadata={
            "name": "GarageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
