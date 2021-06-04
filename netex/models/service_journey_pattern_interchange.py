from dataclasses import dataclass
from netex.models.service_journey_pattern_interchange_version_structure import ServiceJourneyPatternInterchangeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourneyPatternInterchange(ServiceJourneyPatternInterchangeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
