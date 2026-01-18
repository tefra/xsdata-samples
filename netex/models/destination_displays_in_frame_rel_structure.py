from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .destination_display import DestinationDisplay

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DestinationDisplaysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "destinationDisplaysInFrame_RelStructure"

    destination_display: Iterable[DestinationDisplay] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
