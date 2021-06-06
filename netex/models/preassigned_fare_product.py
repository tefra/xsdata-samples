from dataclasses import dataclass
from .preassigned_fare_product_version_structure import PreassignedFareProductVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PreassignedFareProduct(PreassignedFareProductVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
