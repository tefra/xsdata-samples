from dataclasses import dataclass, field
from typing import List, Union
from .cell_ref_1 import CellRef1
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .time_interval_price_ref import TimeIntervalPriceRef
from .time_interval_price_versioned_child_structure import (
    TimeIntervalPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeIntervalPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "timeIntervalPrices_RelStructure"

    time_interval_price_ref_or_time_interval_price_or_cell_ref: List[
        Union[
            TimeIntervalPriceRef,
            TimeIntervalPriceVersionedChildStructure,
            CellRef1,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPrice",
                    "type": TimeIntervalPriceVersionedChildStructure,
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
