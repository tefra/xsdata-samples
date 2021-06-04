from dataclasses import dataclass
from netex.models.vehicle_version_structure import VehicleVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Vehicle(VehicleVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
