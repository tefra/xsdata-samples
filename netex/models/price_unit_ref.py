from dataclasses import dataclass
from netex.models.price_unit_ref_structure import PriceUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PriceUnitRef(PriceUnitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
