from dataclasses import dataclass
from .preassigned_fare_product_ref_structure import (
    PreassignedFareProductRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SupplementProductRefStructure(PreassignedFareProductRefStructure):
    pass
