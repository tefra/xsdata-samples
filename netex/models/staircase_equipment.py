from dataclasses import dataclass
from netex.models.staircase_equipment_version_structure import StaircaseEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StaircaseEquipment(StaircaseEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
