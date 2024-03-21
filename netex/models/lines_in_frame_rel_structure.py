from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_line import FlexibleLine
from .line import Line

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "linesInFrame_RelStructure"

    line: List[Union[FlexibleLine, Line]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLine",
                    "type": FlexibleLine,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Line",
                    "type": Line,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
