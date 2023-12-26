from dataclasses import dataclass
from .sales_notice_assignment_version_structure import (
    SalesNoticeAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesNoticeAssignment(SalesNoticeAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
