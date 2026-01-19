from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .onboard_stay import OnboardStay

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnboardStaysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "onboardStays_RelStructure"

    onboard_stay: Sequence[OnboardStay] = field(
        default_factory=list,
        metadata={
            "name": "OnboardStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
