from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.path_junction import PathJunction
from netex.models.path_junction_ref import PathJunctionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathJunctionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pathJunctions_RelStructure"

    path_junction_ref: List[PathJunctionRef] = field(
        default_factory=list,
        metadata={
            "name": "PathJunctionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_junction: List[PathJunction] = field(
        default_factory=list,
        metadata={
            "name": "PathJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
