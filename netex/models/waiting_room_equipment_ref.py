from __future__ import annotations

from dataclasses import dataclass

from .waiting_room_equipment_ref_structure import (
    WaitingRoomEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WaitingRoomEquipmentRef(WaitingRoomEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
