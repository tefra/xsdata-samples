from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .place_ref_1 import PlaceRef1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "placeRefs_RelStructure"

    place_ref: List[PlaceRef1] = field(
        default_factory=list,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
