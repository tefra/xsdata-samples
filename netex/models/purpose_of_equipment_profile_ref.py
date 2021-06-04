from dataclasses import dataclass
from netex.models.purpose_of_equipment_profile_ref_structure import PurposeOfEquipmentProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PurposeOfEquipmentProfileRef(PurposeOfEquipmentProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
