from dataclasses import dataclass
from .cell_versioned_child_structure import PriceableObjectVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PriceableObject1(PriceableObjectVersionStructure):
    class Meta:
        name = "PriceableObject"
        namespace = "http://www.netex.org.uk/netex"