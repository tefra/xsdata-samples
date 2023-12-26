from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .logical_display import LogicalDisplay

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LogicalDisplaysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "logicalDisplaysInFrame_RelStructure"

    logical_display: List[LogicalDisplay] = field(
        default_factory=list,
        metadata={
            "name": "LogicalDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
