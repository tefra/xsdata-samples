from dataclasses import dataclass
from netex.models.sign_equipment_version_structure import SignEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SignEquipment(SignEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
