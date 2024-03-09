from dataclasses import dataclass

from .vehicle_journey_version_structure import VehicleJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourney1(VehicleJourneyVersionStructure):
    class Meta:
        name = "VehicleJourney"
        namespace = "http://www.netex.org.uk/netex"
