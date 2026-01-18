from __future__ import annotations

from dataclasses import dataclass

from .type_of_sales_offer_package_ref_structure import (
    TypeOfSalesOfferPackageRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfSalesOfferPackageRef(TypeOfSalesOfferPackageRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
