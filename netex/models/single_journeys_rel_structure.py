from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .single_journey import SingleJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SingleJourneysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "singleJourneys_RelStructure"

    single_journey: List[SingleJourney] = field(
        default_factory=list,
        metadata={
            "name": "SingleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
