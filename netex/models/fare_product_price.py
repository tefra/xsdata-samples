from dataclasses import dataclass
from .fare_product_price_versioned_child_structure import (
    FareProductPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareProductPrice(FareProductPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
