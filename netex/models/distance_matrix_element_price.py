from __future__ import annotations

from dataclasses import dataclass

from .distance_matrix_element_price_versioned_child_structure import (
    DistanceMatrixElementPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementPrice(
    DistanceMatrixElementPriceVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
