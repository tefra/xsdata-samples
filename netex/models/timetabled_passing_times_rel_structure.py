from dataclasses import dataclass, field
from typing import List
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .timetabled_passing_time import TimetabledPassingTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimetabledPassingTimesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "timetabledPassingTimes_RelStructure"

    timetabled_passing_time: List[TimetabledPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "TimetabledPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
