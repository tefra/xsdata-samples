from dataclasses import dataclass
from .notice_assignment_derived_view_structure import NoticeAssignmentDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NoticeAssignmentView(NoticeAssignmentDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
