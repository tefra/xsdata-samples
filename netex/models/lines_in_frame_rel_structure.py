from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_line import FlexibleLine
from .line_1 import Line1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "linesInFrame_RelStructure"

    flexible_line: List[FlexibleLine] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLine",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line: List[Line1] = field(
        default_factory=list,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
