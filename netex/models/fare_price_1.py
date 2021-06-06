from dataclasses import dataclass
from .fare_price_versioned_child_structure import FarePriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FarePrice1(FarePriceVersionedChildStructure):
    class Meta:
        name = "FarePrice"
        namespace = "http://www.netex.org.uk/netex"
