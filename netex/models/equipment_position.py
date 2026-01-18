from __future__ import annotations

from dataclasses import dataclass

from .equipment_position_structure import EquipmentPositionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EquipmentPosition(EquipmentPositionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
