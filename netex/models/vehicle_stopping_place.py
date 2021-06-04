from dataclasses import dataclass
from netex.models.vehicle_stopping_place_version_structure import VehicleStoppingPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleStoppingPlace(VehicleStoppingPlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
