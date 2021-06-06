from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .line_network import LineNetwork

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineNetworksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "lineNetworksInFrame_RelStructure"

    line_network: List[LineNetwork] = field(
        default_factory=list,
        metadata={
            "name": "LineNetwork",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
