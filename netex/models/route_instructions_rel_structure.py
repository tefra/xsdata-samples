from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .route_instruction import RouteInstruction
from .route_instruction_ref import RouteInstructionRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteInstructionsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "routeInstructions_RelStructure"

    route_instruction_ref_or_route_instruction: Iterable[
        RouteInstructionRef | RouteInstruction
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RouteInstructionRef",
                    "type": RouteInstructionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteInstruction",
                    "type": RouteInstruction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
