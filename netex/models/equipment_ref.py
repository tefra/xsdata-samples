from __future__ import annotations

from dataclasses import dataclass

from .equipment_ref_structure import EquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EquipmentRef(EquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
