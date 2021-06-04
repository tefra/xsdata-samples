from dataclasses import dataclass
from netex.models.activated_equipment_ref_structure import ActivatedEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivatedEquipmentRef(ActivatedEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
