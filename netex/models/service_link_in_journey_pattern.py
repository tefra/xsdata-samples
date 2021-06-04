from dataclasses import dataclass
from netex.models.service_link_in_journey_pattern_versioned_child_structure import ServiceLinkInJourneyPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceLinkInJourneyPattern(ServiceLinkInJourneyPatternVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
