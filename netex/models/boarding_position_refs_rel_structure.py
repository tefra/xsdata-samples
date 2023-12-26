from dataclasses import dataclass, field
from typing import List
from .boarding_position_ref import BoardingPositionRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BoardingPositionRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "boardingPositionRefs_RelStructure"

    boarding_position_ref: List[BoardingPositionRef] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
