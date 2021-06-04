from dataclasses import dataclass, field
from typing import List
from netex.models.customer import Customer
from netex.models.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomersInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "customersInFrame_RelStructure"

    customer: List[Customer] = field(
        default_factory=list,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
