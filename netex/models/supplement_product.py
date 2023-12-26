from dataclasses import dataclass
from .supplement_product_version_structure import (
    SupplementProductVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SupplementProduct(SupplementProductVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
