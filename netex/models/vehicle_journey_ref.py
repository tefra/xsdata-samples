from dataclasses import dataclass
from .vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyRef(VehicleJourneyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
