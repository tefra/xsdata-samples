from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .coupled_journey_ref import CoupledJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CoupledJourneysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "coupledJourneys_RelStructure"

    coupled_journey_ref: Sequence[CoupledJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "CoupledJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
