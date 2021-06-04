from dataclasses import dataclass
from netex.models.waiting_equipment_version_structure import WaitingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WaitingEquipment(WaitingEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
