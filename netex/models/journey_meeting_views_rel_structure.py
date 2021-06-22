from dataclasses import dataclass, field
from typing import List
from .journey_meeting_ref import JourneyMeetingRef
from .journey_meeting_view import JourneyMeetingView
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyMeetingViewsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "journeyMeetingViews_RelStructure"

    journey_meeting_ref_or_journey_meeting_view: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyMeetingRef",
                    "type": JourneyMeetingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyMeetingView",
                    "type": JourneyMeetingView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
