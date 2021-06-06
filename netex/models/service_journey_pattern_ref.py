from dataclasses import dataclass
from .service_journey_pattern_ref_structure import ServiceJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourneyPatternRef(ServiceJourneyPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
