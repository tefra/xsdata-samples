from dataclasses import dataclass, field
from typing import Optional
from .controllable_element_ref import ControllableElementRef
from .fare_price_versioned_child_structure import FarePriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControllableElementPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "ControllableElementPrice_VersionedChildStructure"

    controllable_element_ref: Optional[ControllableElementRef] = field(
        default=None,
        metadata={
            "name": "ControllableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
