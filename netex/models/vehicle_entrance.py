from dataclasses import dataclass
from .vehicle_entrance_version_structure import VehicleEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEntrance(VehicleEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
