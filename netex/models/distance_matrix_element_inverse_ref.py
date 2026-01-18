from __future__ import annotations

from dataclasses import dataclass

from .distance_matrix_element_ref_structure import (
    DistanceMatrixElementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementInverseRef(DistanceMatrixElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
