from dataclasses import dataclass, field
from typing import List, Union
from .allowed_line_direction import AllowedLineDirection
from .allowed_line_direction_ref import AllowedLineDirectionRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllowedLineDirectionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "allowedLineDirections_RelStructure"

    allowed_line_direction_ref_or_allowed_line_direction: List[
        Union[AllowedLineDirectionRef, AllowedLineDirection]
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
