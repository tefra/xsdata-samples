from dataclasses import dataclass
from netex.models.notice_assignment_version_structure import NoticeAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NoticeAssignment1(NoticeAssignmentVersionStructure):
    class Meta:
        name = "NoticeAssignment"
        namespace = "http://www.netex.org.uk/netex"
