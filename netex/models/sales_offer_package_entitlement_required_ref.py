from __future__ import annotations

from dataclasses import dataclass

from .sales_offer_package_entitlement_required_ref_structure import (
    SalesOfferPackageEntitlementRequiredRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageEntitlementRequiredRef(
    SalesOfferPackageEntitlementRequiredRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
