from __future__ import annotations

from dataclasses import dataclass

from .waiting_equipment_ref_structure import WaitingEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WaitingEquipmentRef(WaitingEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
