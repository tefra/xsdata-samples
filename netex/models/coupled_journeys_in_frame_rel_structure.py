from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.coupled_journey import CoupledJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CoupledJourneysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "coupledJourneysInFrame_RelStructure"

    coupled_journey: List[CoupledJourney] = field(
        default_factory=list,
        metadata={
            "name": "CoupledJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
