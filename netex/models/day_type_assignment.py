from __future__ import annotations

from dataclasses import dataclass

from .day_type_assignment_version_structure import (
    DayTypeAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DayTypeAssignment(DayTypeAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
