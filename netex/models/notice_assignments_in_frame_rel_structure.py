from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .notice_assignment import NoticeAssignment
from .sales_notice_assignment import SalesNoticeAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NoticeAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "noticeAssignmentsInFrame_RelStructure"

    sales_notice_assignment: List[SalesNoticeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SalesNoticeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignment: List[NoticeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "NoticeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
