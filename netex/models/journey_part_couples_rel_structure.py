from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.journey_part_couple import JourneyPartCouple
from netex.models.journey_part_couple_ref import JourneyPartCoupleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartCouplesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyPartCouples_RelStructure"

    journey_part_couple_ref: List[JourneyPartCoupleRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartCoupleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part_couple: List[JourneyPartCouple] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartCouple",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
