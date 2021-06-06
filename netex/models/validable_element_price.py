from dataclasses import dataclass
from .validable_element_price_versioned_child_structure import ValidableElementPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidableElementPrice(ValidableElementPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
