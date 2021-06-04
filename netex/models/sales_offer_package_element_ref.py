from dataclasses import dataclass
from netex.models.sales_offer_package_element_ref_structure import SalesOfferPackageElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageElementRef(SalesOfferPackageElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
