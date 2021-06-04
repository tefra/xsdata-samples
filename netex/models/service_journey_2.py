from dataclasses import dataclass
from netex.models.service_journey_version_structure import ServiceJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourney2(ServiceJourneyVersionStructure):
    class Meta:
        name = "ServiceJourney"
        namespace = "http://www.netex.org.uk/netex"
