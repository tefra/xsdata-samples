from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .network import Network

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "networksInFrame_RelStructure"

    network: Sequence[Network] = field(
        default_factory=list,
        metadata={
            "name": "Network",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
