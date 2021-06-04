from dataclasses import dataclass
from netex.models.seating_equipment_ref_structure import SeatingEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeatingEquipmentRef(SeatingEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
