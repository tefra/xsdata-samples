from dataclasses import dataclass
from .vehicle_service_version_structure import VehicleServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleService(VehicleServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
