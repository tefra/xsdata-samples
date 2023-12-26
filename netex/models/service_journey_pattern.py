from dataclasses import dataclass
from .service_journey_pattern_version_structure import (
    ServiceJourneyPatternVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourneyPattern(ServiceJourneyPatternVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
