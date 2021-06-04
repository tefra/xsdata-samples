from dataclasses import dataclass
from netex.models.cell_versioned_child_structure import PriceableObjectVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PriceableObject2(PriceableObjectVersionStructure):
    class Meta:
        name = "PriceableObject"
        namespace = "http://www.netex.org.uk/netex"
