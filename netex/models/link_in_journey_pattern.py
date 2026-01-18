from __future__ import annotations

from dataclasses import dataclass

from .link_in_journey_pattern_versioned_child_structure import (
    LinkInJourneyPatternVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkInJourneyPattern(LinkInJourneyPatternVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
