from dataclasses import dataclass, field
from typing import Optional
from netex.models.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.models.validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidableElementPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "ValidableElementPrice_VersionedChildStructure"

    validable_element_ref: Optional[ValidableElementRef] = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
