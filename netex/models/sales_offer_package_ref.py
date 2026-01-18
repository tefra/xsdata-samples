from __future__ import annotations

from dataclasses import dataclass

from .sales_offer_package_ref_structure import SalesOfferPackageRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageRef(SalesOfferPackageRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
