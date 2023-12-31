from dataclasses import dataclass, field
from typing import List, Union
from .cell_ref import CellRef
from .sales_offer_package_price_ref import SalesOfferPackagePriceRef
from .sales_offer_package_price_versioned_child_structure import (
    SalesOfferPackagePriceVersionedChildStructure,
)
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackagePricesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "salesOfferPackagePrices_RelStructure"

    sales_offer_package_price_ref_or_sales_offer_package_price_or_cell_ref: List[
        Union[
            SalesOfferPackagePriceRef,
            SalesOfferPackagePriceVersionedChildStructure,
            CellRef,
        ]
    ] = field(
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
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
