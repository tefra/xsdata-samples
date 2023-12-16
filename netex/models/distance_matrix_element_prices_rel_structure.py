from dataclasses import dataclass, field
from typing import List, Union
from .cell_ref import CellRef
from .distance_matrix_element_price import DistanceMatrixElementPrice
from .distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "distanceMatrixElementPrices_RelStructure"

    distance_matrix_element_price_ref_or_distance_matrix_element_price_or_cell_ref: List[Union[DistanceMatrixElementPriceRef, DistanceMatrixElementPrice, CellRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPrice",
                    "type": DistanceMatrixElementPrice,
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
