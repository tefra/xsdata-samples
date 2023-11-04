from dataclasses import dataclass, field
from typing import List, Union
from .cell_ref import CellRef
from .fare_product_price import FareProductPrice
from .fare_product_price_ref import FareProductPriceRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareProductPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareProductPrices_RelStructure"

    fare_product_price_ref_or_cell_ref_or_fare_product_price: List[Union[CellRef, FareProductPriceRef, FareProductPrice]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPrice",
                    "type": FareProductPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
