from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .path_junction import PathJunction
from .path_junction_ref import PathJunctionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathJunctionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pathJunctions_RelStructure"

    path_junction_ref_or_path_junction: Iterable[
        Union[PathJunctionRef, PathJunction]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PathJunctionRef",
                    "type": PathJunctionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathJunction",
                    "type": PathJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
