from __future__ import annotations

from dataclasses import dataclass

from .timing_link_in_journey_pattern_versioned_child_structure import (
    TimingLinkInJourneyPatternVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingLinkInJourneyPattern(
    TimingLinkInJourneyPatternVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
