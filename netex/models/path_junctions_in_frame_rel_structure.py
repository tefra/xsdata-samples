from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .path_junction import PathJunction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathJunctionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pathJunctionsInFrame_RelStructure"

    path_junction: Iterable[PathJunction] = field(
        default_factory=list,
        metadata={
            "name": "PathJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
