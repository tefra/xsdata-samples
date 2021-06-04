from dataclasses import dataclass, field
from typing import Optional
from netex.models.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.models.fare_structure_element_ref import FareStructureElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareStructureElementPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "FareStructureElementPrice_VersionedChildStructure"

    fare_structure_element_ref: Optional[FareStructureElementRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
