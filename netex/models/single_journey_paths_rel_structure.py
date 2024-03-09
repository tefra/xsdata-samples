from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .single_journey_path import SingleJourneyPath

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SingleJourneyPathsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "singleJourneyPaths_RelStructure"

    single_journey_path: List[SingleJourneyPath] = field(
        default_factory=list,
        metadata={
            "name": "SingleJourneyPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
