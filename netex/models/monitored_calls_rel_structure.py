from dataclasses import dataclass, field
from typing import List
from .monitored_call import MonitoredCall
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MonitoredCallsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "monitoredCalls_RelStructure"

    monitored_call: List[MonitoredCall] = field(
        default_factory=list,
        metadata={
            "name": "MonitoredCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        }
    )
