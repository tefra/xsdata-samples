from __future__ import annotations

from dataclasses import dataclass

from .time_demand_type_assignment_ref_structure import (
    TimeDemandTypeAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeDemandTypeAssignmentRef(TimeDemandTypeAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
