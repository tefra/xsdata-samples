from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.timing_pattern import TimingPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPatternsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timingPatternsInFrame_RelStructure"

    timing_pattern: List[TimingPattern] = field(
        default_factory=list,
        metadata={
            "name": "TimingPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
