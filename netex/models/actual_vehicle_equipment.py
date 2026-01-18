from __future__ import annotations

from dataclasses import dataclass

from .actual_vehicle_equipment_version_structure import (
    ActualVehicleEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActualVehicleEquipment(ActualVehicleEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
