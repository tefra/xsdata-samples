from __future__ import annotations

from dataclasses import dataclass

from .flexible_stop_assignment_version_structure import (
    FlexibleStopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleStopAssignment(FlexibleStopAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
