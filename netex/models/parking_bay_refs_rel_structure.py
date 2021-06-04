from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.parking_bay_ref import ParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingBayRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "parkingBayRefs_RelStructure"

    parking_bay_ref: List[ParkingBayRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingBayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
