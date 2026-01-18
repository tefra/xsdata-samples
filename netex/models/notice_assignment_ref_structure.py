from __future__ import annotations

from dataclasses import dataclass

from .assignment_ref_structure import AssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeAssignmentRefStructure(AssignmentRefStructure):
    pass
