from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_part_couple import JourneyPartCouple
from .journey_part_couple_ref import JourneyPartCoupleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartCouplesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyPartCouples_RelStructure"

    journey_part_couple_ref_or_journey_part_couple: List[
        Union[JourneyPartCoupleRef, JourneyPartCouple]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyPartCoupleRef",
                    "type": JourneyPartCoupleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPartCouple",
                    "type": JourneyPartCouple,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
