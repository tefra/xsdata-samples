from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_meeting import JourneyMeeting

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyMeetingsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyMeetingsInFrame_RelStructure"

    journey_meeting: Iterable[JourneyMeeting] = field(
        default_factory=list,
        metadata={
            "name": "JourneyMeeting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
