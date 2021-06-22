from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .notice_assignment_1 import NoticeAssignment1
from .notice_assignment_2 import NoticeAssignment2
from .notice_assignment_view import NoticeAssignmentView
from .sales_notice_assignment import SalesNoticeAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NoticeAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "noticeAssignments_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesNoticeAssignment",
                    "type": SalesNoticeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeAssignment",
                    "type": NoticeAssignment1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeAssignment_",
                    "type": NoticeAssignment2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeAssignmentView",
                    "type": NoticeAssignmentView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
