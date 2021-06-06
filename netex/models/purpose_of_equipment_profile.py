from dataclasses import dataclass
from .purpose_of_equipment_profile_value_structure import PurposeOfEquipmentProfileValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PurposeOfEquipmentProfile(PurposeOfEquipmentProfileValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
