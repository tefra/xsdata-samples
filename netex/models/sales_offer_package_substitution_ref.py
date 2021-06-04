from dataclasses import dataclass
from netex.models.sales_offer_package_substitution_ref_structure import SalesOfferPackageSubstitutionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageSubstitutionRef(SalesOfferPackageSubstitutionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
