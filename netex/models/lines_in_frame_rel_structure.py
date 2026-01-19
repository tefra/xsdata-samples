from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_line import FlexibleLine
from .line import Line

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "linesInFrame_RelStructure"

    line: Sequence[FlexibleLine | Line] = field(
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
