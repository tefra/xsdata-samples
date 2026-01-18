from __future__ import annotations

from dataclasses import dataclass

from .shelter_equipment_version_structure import (
    ShelterEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ShelterEquipment(ShelterEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
