from dataclasses import dataclass, field
from typing import List
from .cell_ref_1 import CellRef1
from .sales_offer_package_price_ref import SalesOfferPackagePriceRef
from .sales_offer_package_price_versioned_child_structure import SalesOfferPackagePriceVersionedChildStructure
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackagePricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "salesOfferPackagePrices_RelStructure"

    sales_offer_package_price_ref_or_sales_offer_package_price_or_cell_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePrice",
                    "type": SalesOfferPackagePriceVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
