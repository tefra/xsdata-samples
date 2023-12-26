from dataclasses import dataclass, field
from typing import List
from .frame_containment_structure import FrameContainmentStructure
from .validity_parameter_assignment import ValidityParameterAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidityParameterAssignmentsInFrameRelStructure(
    FrameContainmentStructure
):
    class Meta:
        name = "validityParameterAssignmentsInFrame_RelStructure"

    validity_parameter_assignment: List[ValidityParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ValidityParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
