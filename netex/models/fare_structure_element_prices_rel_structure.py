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

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPrice",
                    "type": FareStructureElementPriceVersionedChildStructure,
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
            ),
        }
    )
