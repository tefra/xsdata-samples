from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .network import Network

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "networksInFrame_RelStructure"

    network: Iterable[Network] = field(
        default_factory=list,
        metadata={
            "name": "Network",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
