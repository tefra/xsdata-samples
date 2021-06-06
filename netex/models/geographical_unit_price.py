from dataclasses import dataclass
from .geographical_unit_price_versioned_child_structure import GeographicalUnitPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalUnitPrice(GeographicalUnitPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
