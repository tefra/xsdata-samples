from dataclasses import dataclass
from netex.models.group_of_sales_offer_packages_ref_structure import GroupOfSalesOfferPackagesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfSalesOfferPackagesRef(GroupOfSalesOfferPackagesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
