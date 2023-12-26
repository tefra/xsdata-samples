from dataclasses import dataclass
from .type_of_sales_offer_package_version_structure import (
    TypeOfSalesOfferPackageVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfSalesOfferPackage(TypeOfSalesOfferPackageVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
