from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .distance_matrix_element import DistanceMatrixElement
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "distanceMatrixElementsInFrame_RelStructure"

    distance_matrix_element: Iterable[DistanceMatrixElement] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
