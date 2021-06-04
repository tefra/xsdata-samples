from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.parking_area_ref import ParkingAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingAreaRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "parkingAreaRefs_RelStructure"

    parking_area_ref: List[ParkingAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
