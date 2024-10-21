from collections.abc import Iterable
from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .timing_link import TimingLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingLinksRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "timingLinks_RelStructure"

    timing_link: Iterable[TimingLink] = field(
        default_factory=list,
        metadata={
            "name": "TimingLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
