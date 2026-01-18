from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .validity_parameter_assignment import ValidityParameterAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityParameterAssignmentsInFrameRelStructure(
    FrameContainmentStructure
):
    class Meta:
        name = "validityParameterAssignmentsInFrame_RelStructure"

    validity_parameter_assignment: Iterable[ValidityParameterAssignment] = (
        field(
            default_factory=list,
            metadata={
                "name": "ValidityParameterAssignment",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
