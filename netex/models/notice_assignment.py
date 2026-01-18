from __future__ import annotations

from dataclasses import dataclass

from .notice_assignment_version_structure import (
    NoticeAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeAssignment(NoticeAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
