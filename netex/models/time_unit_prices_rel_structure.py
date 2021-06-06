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

    time_unit_price_ref: List[TimeUnitPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeUnitPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_unit_price: List[TimeUnitPriceVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "TimeUnitPrice",
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
