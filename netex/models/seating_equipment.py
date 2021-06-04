from dataclasses import dataclass
from netex.models.seating_equipment_version_structure import SeatingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeatingEquipment(SeatingEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
