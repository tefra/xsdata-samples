from __future__ import annotations

from dataclasses import dataclass

from .charging_equipment_profile_version_structure import (
    ChargingEquipmentProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingEquipmentProfile(ChargingEquipmentProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
