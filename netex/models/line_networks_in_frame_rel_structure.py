from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .line_network import LineNetwork

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineNetworksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "lineNetworksInFrame_RelStructure"

    line_network: Iterable[LineNetwork] = field(
        default_factory=list,
        metadata={
            "name": "LineNetwork",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
