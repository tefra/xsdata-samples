from dataclasses import dataclass
from netex.models.waiting_room_equipment_version_structure import WaitingRoomEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WaitingRoomEquipment(WaitingRoomEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
