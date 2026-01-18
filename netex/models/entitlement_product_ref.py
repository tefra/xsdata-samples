from __future__ import annotations

from dataclasses import dataclass

from .entitlement_product_ref_structure import EntitlementProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntitlementProductRef(EntitlementProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
