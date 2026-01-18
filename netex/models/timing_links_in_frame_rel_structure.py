from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .timing_link import TimingLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingLinksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timingLinksInFrame_RelStructure"

    timing_link: Iterable[TimingLink] = field(
        default_factory=list,
        metadata={
            "name": "TimingLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
