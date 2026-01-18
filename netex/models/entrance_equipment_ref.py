from __future__ import annotations

from dataclasses import dataclass

from .entrance_equipment_ref_structure import EntranceEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntranceEquipmentRef(EntranceEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
