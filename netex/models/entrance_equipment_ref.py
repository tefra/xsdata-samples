from dataclasses import dataclass
from netex.models.entrance_equipment_ref_structure import EntranceEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntranceEquipmentRef(EntranceEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
