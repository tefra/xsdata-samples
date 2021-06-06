from dataclasses import dataclass, field
from typing import List
from .log_entry import LogEntry
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LogEntriesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "logEntries_RelStructure"

    log_entry: List[LogEntry] = field(
        default_factory=list,
        metadata={
            "name": "LogEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
