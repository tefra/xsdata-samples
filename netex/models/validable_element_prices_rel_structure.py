from dataclasses import dataclass, field
from typing import List, Union
from .cell_ref_1 import CellRef1
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .validable_element_price import ValidableElementPrice
from .validable_element_price_ref import ValidableElementPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidableElementPricesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "validableElementPrices_RelStructure"

    validable_element_price_ref_or_validable_element_price_or_cell_ref: List[
        Union[ValidableElementPriceRef, ValidableElementPrice, CellRef1]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPrice",
                    "type": ValidableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
