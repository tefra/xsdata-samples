from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .notice_assignment import NoticeAssignment
from .notice_assignment_view import NoticeAssignmentView
from .sales_notice_assignment import SalesNoticeAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NoticeAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "noticeAssignments_RelStructure"

    sales_notice_assignment_or_notice_assignment_or_notice_assignment_view: Iterable[
        SalesNoticeAssignment | NoticeAssignment | NoticeAssignmentView
    ] = field(
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
                    "type": NoticeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeAssignmentView",
                    "type": NoticeAssignmentView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
