from dataclasses import dataclass
from netex.models.fare_price_versioned_child_structure import FarePriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FarePrice2(FarePriceVersionedChildStructure):
    class Meta:
        name = "FarePrice"
        namespace = "http://www.netex.org.uk/netex"
