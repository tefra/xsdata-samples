from __future__ import annotations

from dataclasses import dataclass

from .distance_matrix_element_price_ref_structure import (
    DistanceMatrixElementPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementPriceRef(DistanceMatrixElementPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
