from dataclasses import dataclass
from netex.models.trolley_stand_equipment_ref_structure import TrolleyStandEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrolleyStandEquipmentRef(TrolleyStandEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
