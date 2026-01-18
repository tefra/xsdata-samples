from __future__ import annotations

from dataclasses import dataclass

from .equipment_position_ref_structure import EquipmentPositionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EquipmentPositionRef(EquipmentPositionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
