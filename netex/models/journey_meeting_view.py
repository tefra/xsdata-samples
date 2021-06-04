from dataclasses import dataclass
from netex.models.journey_meeting_derived_view_structure import JourneyMeetingDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyMeetingView(JourneyMeetingDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
