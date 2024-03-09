from dataclasses import dataclass

from .entitlement_product_version_structure import (
    EntitlementProductVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntitlementProduct(EntitlementProductVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
