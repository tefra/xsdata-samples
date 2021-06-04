from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.destination_display import DestinationDisplay

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DestinationDisplaysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "destinationDisplaysInFrame_RelStructure"

    destination_display: List[DestinationDisplay] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
