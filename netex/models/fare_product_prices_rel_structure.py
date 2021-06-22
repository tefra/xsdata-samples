from dataclasses import dataclass, field
from typing import List
from .cell_ref_1 import CellRef1
from .cell_ref_2 import CellRef2
from .fare_product_price import FareProductPrice
from .fare_product_price_ref import FareProductPriceRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareProductPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareProductPrices_RelStructure"

    choice: List[object] = field(
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
                    "type": CellRef1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef_",
                    "type": CellRef2,
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
