from dataclasses import dataclass, field
from typing import List
from netex.models.journey_meeting_ref import JourneyMeetingRef
from netex.models.journey_meeting_view import JourneyMeetingView
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyMeetingViewsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "journeyMeetingViews_RelStructure"

    journey_meeting_ref: List[JourneyMeetingRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyMeetingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_meeting_view: List[JourneyMeetingView] = field(
        default_factory=list,
        metadata={
            "name": "JourneyMeetingView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
