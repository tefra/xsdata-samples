from dataclasses import dataclass, field
from typing import List
from .cell_ref_1 import CellRef1
from .cell_ref_2 import CellRef2
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .time_interval_price_ref import TimeIntervalPriceRef
from .time_interval_price_versioned_child_structure import TimeIntervalPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeIntervalPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "timeIntervalPrices_RelStructure"

    time_interval_price_ref: List[TimeIntervalPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeIntervalPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_interval_price: List[TimeIntervalPriceVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "TimeIntervalPrice",
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
