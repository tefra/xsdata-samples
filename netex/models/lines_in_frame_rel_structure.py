from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_line import FlexibleLine
from .line_1 import Line1
from .line_2 import Line2

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
            "min_occurs": 1,
        }
    )
    line: List[Line1] = field(
        default_factory=list,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_line: List[Line2] = field(
        default_factory=list,
        metadata={
            "name": "Line_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
