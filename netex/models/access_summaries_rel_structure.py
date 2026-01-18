from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .access_summary import AccessSummary
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessSummariesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "accessSummaries_RelStructure"

    access_summary: Iterable[AccessSummary] = field(
        default_factory=list,
        metadata={
            "name": "AccessSummary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
