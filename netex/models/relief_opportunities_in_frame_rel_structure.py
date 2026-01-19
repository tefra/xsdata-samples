from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .relief_opportunity import ReliefOpportunity

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefOpportunitiesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "reliefOpportunitiesInFrame_RelStructure"

    relief_opportunity: Sequence[ReliefOpportunity] = field(
        default_factory=list,
        metadata={
            "name": "ReliefOpportunity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
