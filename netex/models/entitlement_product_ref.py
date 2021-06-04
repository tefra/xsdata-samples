from dataclasses import dataclass
from netex.models.entitlement_product_ref_structure import EntitlementProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntitlementProductRef(EntitlementProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
