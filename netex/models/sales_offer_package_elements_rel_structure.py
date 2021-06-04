from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_element_ref import SalesOfferPackageElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageElementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "salesOfferPackageElements_RelStructure"

    sales_offer_package_element_ref: List[SalesOfferPackageElementRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_element: List[SalesOfferPackageElement] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
