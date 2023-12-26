from dataclasses import dataclass
from .geographical_unit_price_ref_structure import (
    GeographicalUnitPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalUnitPriceRef(GeographicalUnitPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
