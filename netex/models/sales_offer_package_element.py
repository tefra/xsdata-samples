from __future__ import annotations

from dataclasses import dataclass

from .sales_offer_package_element_version_structure import (
    SalesOfferPackageElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageElement(SalesOfferPackageElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
