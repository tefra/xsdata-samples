from dataclasses import dataclass

from .vehicle_equipment_profile_ref_structure import (
    VehicleEquipmentProfileRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ChargingEquipmentProfileRefStructure(
    VehicleEquipmentProfileRefStructure
):
    pass
