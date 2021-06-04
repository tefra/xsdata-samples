from dataclasses import dataclass
from netex.models.fare_product_ref_structure import FareProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareProductRef(FareProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
