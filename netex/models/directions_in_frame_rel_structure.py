from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .direction import Direction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DirectionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "directionsInFrame_RelStructure"

    direction: Iterable[Direction] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
