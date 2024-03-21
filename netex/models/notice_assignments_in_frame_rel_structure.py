from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .notice_assignment import NoticeAssignment
from .sales_notice_assignment import SalesNoticeAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NoticeAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "noticeAssignmentsInFrame_RelStructure"

    notice_assignment: List[Union[SalesNoticeAssignment, NoticeAssignment]] = (
        field(
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
                ),
            },
        )
    )
