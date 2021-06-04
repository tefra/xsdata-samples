from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.coupled_journey_ref import CoupledJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CoupledJourneysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "coupledJourneys_RelStructure"

    coupled_journey_ref: List[CoupledJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "CoupledJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
