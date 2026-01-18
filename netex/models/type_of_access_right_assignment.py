from __future__ import annotations

from dataclasses import dataclass

from .type_of_access_right_assignment_version_structure import (
    TypeOfAccessRightAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfAccessRightAssignment(TypeOfAccessRightAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
