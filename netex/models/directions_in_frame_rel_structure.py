from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.direction import Direction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DirectionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "directionsInFrame_RelStructure"

    direction: List[Direction] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
