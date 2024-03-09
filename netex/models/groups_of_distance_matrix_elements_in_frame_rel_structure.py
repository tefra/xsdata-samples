from dataclasses import dataclass, field
from typing import List

from .distance_matrix_element import DistanceMatrixElement
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupsOfDistanceMatrixElementsInFrameRelStructure(
    FrameContainmentStructure
):
    class Meta:
        name = "groupsOfDistanceMatrixElementsInFrame_RelStructure"

    distance_matrix_element: List[DistanceMatrixElement] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
