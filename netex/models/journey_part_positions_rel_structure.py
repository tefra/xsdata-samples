from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_part_position import JourneyPartPosition

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartPositionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyPartPositions_RelStructure"

    journey_part_position: List[JourneyPartPosition] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
