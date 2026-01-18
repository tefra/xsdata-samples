from __future__ import annotations

from dataclasses import dataclass

from .access_right_parameter_assignment_version_structure import (
    AccessRightParameterAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessRightParameterAssignment(
    AccessRightParameterAssignmentVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
