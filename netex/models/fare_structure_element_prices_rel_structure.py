from dataclasses import dataclass, field
from typing import List
from .cell_ref_1 import CellRef1
from .cell_ref_2 import CellRef2
from .fare_structure_element_price_ref import FareStructureElementPriceRef
from .fare_structure_element_price_versioned_child_structure import FareStructureElementPriceVersionedChildStructure
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareStructureElementPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareStructureElementPrices_RelStructure"

    fare_structure_element_price_ref: List[FareStructureElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_element_price: List[FareStructureElementPriceVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementPrice",
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
