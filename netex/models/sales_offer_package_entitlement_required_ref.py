from dataclasses import dataclass
from .sales_offer_package_entitlement_required_ref_structure import (
    SalesOfferPackageEntitlementRequiredRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageEntitlementRequiredRef(
    SalesOfferPackageEntitlementRequiredRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
