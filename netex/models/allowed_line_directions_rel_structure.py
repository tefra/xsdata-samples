from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .allowed_line_direction import AllowedLineDirection
from .allowed_line_direction_ref import AllowedLineDirectionRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllowedLineDirectionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "allowedLineDirections_RelStructure"

    allowed_line_direction_ref_or_allowed_line_direction: Sequence[
        AllowedLineDirectionRef | AllowedLineDirection
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllowedLineDirectionRef",
                    "type": AllowedLineDirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllowedLineDirection",
                    "type": AllowedLineDirection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
