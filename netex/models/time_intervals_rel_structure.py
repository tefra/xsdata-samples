from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.time_interval import TimeInterval
from netex.models.time_interval_ref import TimeIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeIntervalsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timeIntervals_RelStructure"

    time_interval_ref: List[TimeIntervalRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_interval: List[TimeInterval] = field(
        default_factory=list,
        metadata={
            "name": "TimeInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
