from dataclasses import dataclass, field
from typing import List
from netex.models.cell_ref_1 import CellRef1
from netex.models.cell_ref_2 import CellRef2
from netex.models.cell_versioned_child_structure import ParkingPriceVersionedChildStructure
from netex.models.parking_price_ref import ParkingPriceRef
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "parkingPrices_RelStructure"

    parking_price_ref: List[ParkingPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPriceRef",
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
    parking_price: List[ParkingPriceVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
