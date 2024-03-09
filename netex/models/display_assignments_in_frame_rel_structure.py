from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .display_assignment import DisplayAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DisplayAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "displayAssignmentsInFrame_RelStructure"

    display_assignment: List[DisplayAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DisplayAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
