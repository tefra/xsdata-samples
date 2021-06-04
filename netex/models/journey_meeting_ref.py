from dataclasses import dataclass
from netex.models.journey_meeting_ref_structure import JourneyMeetingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyMeetingRef(JourneyMeetingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
