from dataclasses import dataclass
from netex.models.dated_vehicle_journey_version_structure import DatedVehicleJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedVehicleJourney(DatedVehicleJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
