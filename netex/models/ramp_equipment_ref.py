from dataclasses import dataclass
from netex.models.access_equipment_ref_structure import AccessEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RampEquipmentRef(AccessEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
