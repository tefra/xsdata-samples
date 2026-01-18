from __future__ import annotations

from dataclasses import dataclass

from .timing_link_in_journey_pattern_ref_structure import (
    TimingLinkInJourneyPatternRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingLinkInJourneyPatternRef(TimingLinkInJourneyPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
