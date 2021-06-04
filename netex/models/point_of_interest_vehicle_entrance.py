from dataclasses import dataclass
from netex.models.point_of_interest_vehicle_entrance_version_structure import PointOfInterestVehicleEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestVehicleEntrance(PointOfInterestVehicleEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
