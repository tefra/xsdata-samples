from dataclasses import dataclass
from netex.models.vehicle_service_part_version_structure import VehicleServicePartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleServicePart(VehicleServicePartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
