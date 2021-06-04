from dataclasses import dataclass
from netex.models.lift_equipment_version_structure import LiftEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LiftEquipment(LiftEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
