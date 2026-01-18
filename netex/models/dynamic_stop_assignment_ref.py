from __future__ import annotations

from dataclasses import dataclass

from .dynamic_stop_assignment_ref_structure import (
    DynamicStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DynamicStopAssignmentRef(DynamicStopAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
