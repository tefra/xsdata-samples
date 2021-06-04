from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.sales_offer_package_substitution import SalesOfferPackageSubstitution
from netex.models.sales_offer_package_substitution_ref import SalesOfferPackageSubstitutionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageSubstitutionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "salesOfferPackageSubstitutions_RelStructure"

    sales_offer_package_substitution_ref: List[SalesOfferPackageSubstitutionRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageSubstitutionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_substitution: List[SalesOfferPackageSubstitution] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageSubstitution",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
