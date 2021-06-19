from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .notice import Notice
from .notice_ref import NoticeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NoticesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "notices_RelStructure"

    notice_ref_or_notice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NoticeRef",
                    "type": NoticeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Notice",
                    "type": Notice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
