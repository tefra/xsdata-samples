from dataclasses import dataclass
from .sales_offer_package_entitlement_given_version_structure import (
    SalesOfferPackageEntitlementGivenVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageEntitlementGiven(
    SalesOfferPackageEntitlementGivenVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
