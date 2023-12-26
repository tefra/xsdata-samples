from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .point_of_interest_ref import PointOfInterestRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "pointOfInterestRefs_RelStructure"

    point_of_interest_ref: List[PointOfInterestRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
