from __future__ import annotations

from dataclasses import dataclass

from .path_assignment_ref_structure import PathAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathAssignmentRef(PathAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
