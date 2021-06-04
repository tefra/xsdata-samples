from dataclasses import dataclass
from netex.models.supplement_product_ref_structure import SupplementProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SupplementProductRef(SupplementProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
