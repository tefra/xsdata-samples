from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.timing_link import TimingLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingLinksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timingLinksInFrame_RelStructure"

    timing_link: List[TimingLink] = field(
        default_factory=list,
        metadata={
            "name": "TimingLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
