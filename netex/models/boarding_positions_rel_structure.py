from dataclasses import dataclass, field
from typing import List
from .boarding_position import BoardingPosition
from .boarding_position_ref import BoardingPositionRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BoardingPositionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "boardingPositions_RelStructure"

    boarding_position_ref: List[BoardingPositionRef] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_position: List[BoardingPosition] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
