from dataclasses import dataclass
from netex.models.luggage_locker_equipment_version_structure import LuggageLockerEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LuggageLockerEquipment(LuggageLockerEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
