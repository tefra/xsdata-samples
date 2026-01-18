from __future__ import annotations

from dataclasses import dataclass

from .day_type_assignment_ref_structure import DayTypeAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DayTypeAssignmentRef(DayTypeAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
