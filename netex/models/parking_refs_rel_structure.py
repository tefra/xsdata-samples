from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .parking_ref import ParkingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "parkingRefs_RelStructure"

    parking_ref: List[ParkingRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
