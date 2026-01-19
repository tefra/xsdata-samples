from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .timing_pattern import TimingPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPatternsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timingPatternsInFrame_RelStructure"

    timing_pattern: Sequence[TimingPattern] = field(
        default_factory=list,
        metadata={
            "name": "TimingPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
