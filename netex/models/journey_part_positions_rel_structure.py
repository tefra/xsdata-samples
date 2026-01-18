from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_part_position import JourneyPartPosition

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPartPositionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyPartPositions_RelStructure"

    journey_part_position: Iterable[JourneyPartPosition] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
