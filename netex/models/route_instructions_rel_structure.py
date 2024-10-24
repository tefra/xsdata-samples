from collections.abc import Iterable
from dataclasses import dataclass, field

from .route_instruction import RouteInstruction
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteInstructionsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "routeInstructions_RelStructure"

    route_instruction: Iterable[RouteInstruction] = field(
        default_factory=list,
        metadata={
            "name": "RouteInstruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
