from dataclasses import dataclass, field
from typing import List, Union
from .cell_ref import CellRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .time_unit_price_ref import TimeUnitPriceRef
from .time_unit_price_versioned_child_structure import TimeUnitPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeUnitPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "timeUnitPrices_RelStructure"

    time_unit_price_ref_or_time_unit_price_or_cell_ref: List[Union[TimeUnitPriceRef, TimeUnitPriceVersionedChildStructure, CellRef]] = field(
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
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
