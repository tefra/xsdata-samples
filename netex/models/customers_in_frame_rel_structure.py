from collections.abc import Iterable
from dataclasses import dataclass, field

from .customer import Customer
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomersInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "customersInFrame_RelStructure"

    customer: Iterable[Customer] = field(
        default_factory=list,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
