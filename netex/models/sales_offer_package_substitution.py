from __future__ import annotations

from dataclasses import dataclass

from .sales_offer_package_substitution_version_structure import (
    SalesOfferPackageSubstitutionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageSubstitution(
    SalesOfferPackageSubstitutionVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
