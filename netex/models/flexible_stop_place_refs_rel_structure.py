from dataclasses import dataclass, field
from typing import List

from .flexible_stop_place_ref import FlexibleStopPlaceRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleStopPlaceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "flexibleStopPlaceRefs_RelStructure"

    flexible_stop_place_ref: List[FlexibleStopPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
