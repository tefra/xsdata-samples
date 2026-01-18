from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .notice import Notice
from .notice_ref import NoticeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "notices_RelStructure"

    notice_ref_or_notice: Iterable[NoticeRef | Notice] = field(
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
        },
    )
