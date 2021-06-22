from dataclasses import dataclass, field
from typing import List
from .cell_ref_1 import CellRef1
from .cell_ref_2 import CellRef2
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .time_unit_price_ref import TimeUnitPriceRef
from .time_unit_price_versioned_child_structure import TimeUnitPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeUnitPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "timeUnitPrices_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeUnitPriceRef",
                    "type": TimeUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPrice",
                    "type": TimeUnitPriceVersionedChildStructure,
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
