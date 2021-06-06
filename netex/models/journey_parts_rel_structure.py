from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_part import JourneyPart
from .journey_part_ref import JourneyPartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyParts_RelStructure"

    journey_part_ref: List[JourneyPartRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part: List[JourneyPart] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
