from dataclasses import dataclass
from netex.models.escalator_equipment_version_structure import EscalatorEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EscalatorEquipment(EscalatorEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
