from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.topographic_place_ref_structure import TopographicPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopographicPlaceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "topographicPlaceRefs_RelStructure"

    topographic_place_ref: List[TopographicPlaceRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
