from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .distance_matrix_element import DistanceMatrixElement
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfDistanceMatrixElementsInFrameRelStructure(
    FrameContainmentStructure
):
    class Meta:
        name = "groupsOfDistanceMatrixElementsInFrame_RelStructure"

    distance_matrix_element: Sequence[DistanceMatrixElement] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
