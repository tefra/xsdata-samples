from __future__ import annotations

from dataclasses import dataclass

from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LogEntriesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "logEntries_RelStructure"
