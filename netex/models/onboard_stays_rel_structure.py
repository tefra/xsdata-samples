from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .onboard_stay import OnboardStay

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnboardStaysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "onboardStays_RelStructure"

    onboard_stay: List[OnboardStay] = field(
        default_factory=list,
        metadata={
            "name": "OnboardStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
