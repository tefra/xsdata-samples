from dataclasses import dataclass

from .group_of_sales_offer_packages_version_structure import (
    GroupOfSalesOfferPackagesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfSalesOfferPackages(GroupOfSalesOfferPackagesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
