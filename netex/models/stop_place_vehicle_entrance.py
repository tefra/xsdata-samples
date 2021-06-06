from dataclasses import dataclass
from .stop_place_vehicle_entrance_version_structure import StopPlaceVehicleEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceVehicleEntrance(StopPlaceVehicleEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
