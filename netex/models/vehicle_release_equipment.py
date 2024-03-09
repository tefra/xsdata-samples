from dataclasses import dataclass

from .vehicle_release_equipment_version_structure import (
    VehicleReleaseEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleReleaseEquipment(VehicleReleaseEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
