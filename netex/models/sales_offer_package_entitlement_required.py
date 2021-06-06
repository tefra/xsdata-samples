from dataclasses import dataclass
from .sales_offer_package_entitlement_required_version_structure import SalesOfferPackageEntitlementRequiredVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageEntitlementRequired(SalesOfferPackageEntitlementRequiredVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
