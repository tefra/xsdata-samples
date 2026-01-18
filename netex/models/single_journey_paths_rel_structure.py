from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .single_journey_path import SingleJourneyPath

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleJourneyPathsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "singleJourneyPaths_RelStructure"

    single_journey_path: Iterable[SingleJourneyPath] = field(
        default_factory=list,
        metadata={
            "name": "SingleJourneyPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
