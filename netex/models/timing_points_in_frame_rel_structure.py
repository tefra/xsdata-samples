from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.timing_point_1 import TimingPoint1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timingPointsInFrame_RelStructure"

    timing_point: List[TimingPoint1] = field(
        default_factory=list,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
