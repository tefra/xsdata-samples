from __future__ import annotations

from dataclasses import dataclass

from .charging_equipment_profile_ref_structure import (
    ChargingEquipmentProfileRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ChargingEquipmentProfileRef(ChargingEquipmentProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
