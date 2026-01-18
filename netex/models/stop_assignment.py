from __future__ import annotations

from dataclasses import dataclass

from .stop_assignment_version_structure import StopAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopAssignment(StopAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
