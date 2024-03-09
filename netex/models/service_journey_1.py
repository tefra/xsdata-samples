from dataclasses import dataclass

from .service_journey_version_structure import ServiceJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourney1(ServiceJourneyVersionStructure):
    class Meta:
        name = "ServiceJourney"
        namespace = "http://www.netex.org.uk/netex"
