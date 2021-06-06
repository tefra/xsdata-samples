from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_part_couple import JourneyPartCouple

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartCouplesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyPartCouplesInFrame_RelStructure"

    journey_part_couple: List[JourneyPartCouple] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartCouple",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
