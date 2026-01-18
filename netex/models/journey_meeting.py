from __future__ import annotations

from dataclasses import dataclass

from .journey_meeting_version_structure import JourneyMeetingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyMeeting(JourneyMeetingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
