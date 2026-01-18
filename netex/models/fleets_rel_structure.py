from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .fleet import Fleet

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FleetsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fleets_RelStructure"

    fleet: Iterable[Fleet] = field(
        default_factory=list,
        metadata={
            "name": "Fleet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
