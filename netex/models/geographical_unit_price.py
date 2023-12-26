from dataclasses import dataclass
from .geographical_unit_prices_rel_structure import (
    GeographicalUnitPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalUnitPrice(GeographicalUnitPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
