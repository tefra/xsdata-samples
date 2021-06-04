from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.notice_assignment_1 import NoticeAssignment1
from netex.models.notice_assignment_2 import NoticeAssignment2
from netex.models.notice_assignment_view import NoticeAssignmentView
from netex.models.sales_notice_assignment import SalesNoticeAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NoticeAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "noticeAssignments_RelStructure"

    sales_notice_assignment: List[SalesNoticeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SalesNoticeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignment: List[NoticeAssignment2] = field(
        default_factory=list,
        metadata={
            "name": "NoticeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_notice_assignment: List[NoticeAssignment1] = field(
        default_factory=list,
        metadata={
            "name": "NoticeAssignment_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignment_view: List[NoticeAssignmentView] = field(
        default_factory=list,
        metadata={
            "name": "NoticeAssignmentView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
