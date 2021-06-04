from dataclasses import dataclass
from netex.models.link_in_journey_pattern_ref_structure import LinkInJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkInJourneyPatternRef(LinkInJourneyPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
