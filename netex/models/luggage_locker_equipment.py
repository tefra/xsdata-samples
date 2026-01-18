from __future__ import annotations

from dataclasses import dataclass

from .luggage_locker_equipment_version_structure import (
    LuggageLockerEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageLockerEquipment(LuggageLockerEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
