from dataclasses import dataclass, field
from typing import List
from netex.models.allowed_line_direction import AllowedLineDirection
from netex.models.allowed_line_direction_ref import AllowedLineDirectionRef
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllowedLineDirectionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "allowedLineDirections_RelStructure"

    allowed_line_direction_ref: List[AllowedLineDirectionRef] = field(
        default_factory=list,
        metadata={
            "name": "AllowedLineDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    allowed_line_direction: List[AllowedLineDirection] = field(
        default_factory=list,
        metadata={
            "name": "AllowedLineDirection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
