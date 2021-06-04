from dataclasses import dataclass
from netex.models.link_in_journey_pattern_versioned_child_structure import LinkInJourneyPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkInJourneyPattern(LinkInJourneyPatternVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
