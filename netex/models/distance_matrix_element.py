from __future__ import annotations

from dataclasses import dataclass

from .distance_matrix_element_version_structure import (
    DistanceMatrixElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElement(DistanceMatrixElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
