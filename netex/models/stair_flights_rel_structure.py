from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .stair_flight import StairFlight
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StairFlightsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "stairFlights_RelStructure"

    stair_flight: Iterable[StairFlight] = field(
        default_factory=list,
        metadata={
            "name": "StairFlight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
