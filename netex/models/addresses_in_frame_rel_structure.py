from dataclasses import dataclass, field
from typing import List
from netex.models.address import Address
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.postal_address import PostalAddress
from netex.models.road_address import RoadAddress

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AddressesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "addressesInFrame_RelStructure"

    postal_address: List[PostalAddress] = field(
        default_factory=list,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    road_address: List[RoadAddress] = field(
        default_factory=list,
        metadata={
            "name": "RoadAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
