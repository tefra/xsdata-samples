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

    notice_ref: List[NoticeRef] = field(
        default_factory=list,
        metadata={
            "name": "NoticeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice: List[Notice] = field(
        default_factory=list,
        metadata={
            "name": "Notice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
