from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .postal_address import PostalAddress
from .road_address import RoadAddress

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AddressesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "addressesInFrame_RelStructure"

    postal_address_or_road_address: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PostalAddress",
                    "type": PostalAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddress",
                    "type": RoadAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
