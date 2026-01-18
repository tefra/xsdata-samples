from __future__ import annotations

from dataclasses import dataclass

from .group_of_sales_offer_packages_ref_structure import (
    GroupOfSalesOfferPackagesRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfSalesOfferPackagesRef(GroupOfSalesOfferPackagesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
