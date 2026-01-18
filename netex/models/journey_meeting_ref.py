from __future__ import annotations

from dataclasses import dataclass

from .journey_meeting_ref_structure import JourneyMeetingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyMeetingRef(JourneyMeetingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
