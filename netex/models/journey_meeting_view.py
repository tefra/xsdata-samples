from __future__ import annotations

from dataclasses import dataclass

from .journey_meeting_derived_view_structure import (
    JourneyMeetingDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyMeetingView(JourneyMeetingDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
