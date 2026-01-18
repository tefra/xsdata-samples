from __future__ import annotations

from dataclasses import dataclass

from .access_right_parameter_assignment_ref_structure import (
    AccessRightParameterAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControlParameterAssignmentRefStructure(
    AccessRightParameterAssignmentRefStructure
):
    pass
