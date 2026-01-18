from __future__ import annotations

from dataclasses import dataclass

from .notice_assignment_ref_structure import NoticeAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesNoticeAssignmentRefStructure(NoticeAssignmentRefStructure):
    pass
