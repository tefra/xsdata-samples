from dataclasses import dataclass
from netex.models.fare_structure_element_price_ref_structure import FareStructureElementPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareStructureElementPriceRef(FareStructureElementPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
