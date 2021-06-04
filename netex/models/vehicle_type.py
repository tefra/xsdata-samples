from dataclasses import dataclass
from netex.models.vehicle_type_version_structure import VehicleTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleType(VehicleTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
