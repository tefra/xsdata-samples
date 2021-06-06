from dataclasses import dataclass
from .price_group_ref_structure import PriceGroupRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PriceGroupRef(PriceGroupRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
