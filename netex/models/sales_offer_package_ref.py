from dataclasses import dataclass
from .sales_offer_package_ref_structure import SalesOfferPackageRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageRef(SalesOfferPackageRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
