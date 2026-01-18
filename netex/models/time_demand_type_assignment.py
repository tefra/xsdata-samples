from __future__ import annotations

from dataclasses import dataclass

from .time_demand_type_assignment_version_structure import (
    TimeDemandTypeAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandTypeAssignment(TimeDemandTypeAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
