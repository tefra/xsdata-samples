from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .timing_point_1 import TimingPoint1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPointsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timingPoints_RelStructure"

    timing_point: List[TimingPoint1] = field(
        default_factory=list,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )