from dataclasses import dataclass
from netex.models.sales_offer_package_entitlement_given_ref_structure import SalesOfferPackageEntitlementGivenRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageEntitlementGivenRef(SalesOfferPackageEntitlementGivenRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
