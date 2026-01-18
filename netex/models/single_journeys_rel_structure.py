from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .single_journey import SingleJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleJourneysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "singleJourneys_RelStructure"

    single_journey: Iterable[SingleJourney] = field(
        default_factory=list,
        metadata={
            "name": "SingleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
