from dataclasses import dataclass, field
from typing import List
from .cell_ref_1 import CellRef1
from .cell_ref_2 import CellRef2
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .validable_element_price import ValidableElementPrice
from .validable_element_price_ref import ValidableElementPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidableElementPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "validableElementPrices_RelStructure"

    validable_element_price_ref: List[ValidableElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_element_price: List[ValidableElementPrice] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElementPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cell_ref: List[CellRef1] = field(
        default_factory=list,
        metadata={
            "name": "CellRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_cell_ref: List[CellRef2] = field(
        default_factory=list,
        metadata={
            "name": "CellRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )