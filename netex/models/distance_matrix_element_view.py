from __future__ import annotations

from dataclasses import dataclass

from .distance_matrix_element_derived_view_structure import (
    DistanceMatrixElementDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementView(DistanceMatrixElementDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
