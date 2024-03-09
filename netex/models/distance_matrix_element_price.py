from dataclasses import dataclass

from .distance_matrix_element_price_versioned_child_structure import (
    DistanceMatrixElementPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementPrice(
    DistanceMatrixElementPriceVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
