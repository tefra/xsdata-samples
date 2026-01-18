from __future__ import annotations

from dataclasses import dataclass

from .stair_equipment_version_structure import StairEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StairEquipment(StairEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
