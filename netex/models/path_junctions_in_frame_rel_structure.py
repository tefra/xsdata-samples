from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.path_junction import PathJunction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathJunctionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pathJunctionsInFrame_RelStructure"

    path_junction: List[PathJunction] = field(
        default_factory=list,
        metadata={
            "name": "PathJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
