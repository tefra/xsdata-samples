from dataclasses import dataclass
from netex.models.sanitary_equipment_ref_structure import SanitaryEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SanitaryEquipmentRef(SanitaryEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
