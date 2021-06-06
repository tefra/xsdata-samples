from dataclasses import dataclass
from .fare_structure_element_price_versioned_child_structure import FareStructureElementPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareStructureElementPrice(FareStructureElementPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
