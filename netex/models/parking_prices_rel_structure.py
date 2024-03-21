from dataclasses import dataclass, field
from typing import List, Union

from .cell_ref import CellRef
from .parking_price_ref import ParkingPriceRef
from .priceable_object_version_structure import (
    ParkingPriceVersionedChildStructure,
)
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "parkingPrices_RelStructure"

    parking_price_ref_or_cell_ref_or_parking_price: List[
        Union[ParkingPriceRef, CellRef, ParkingPriceVersionedChildStructure]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPrice",
                    "type": ParkingPriceVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
