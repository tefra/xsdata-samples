from dataclasses import dataclass

from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PurposeOfEquipmentProfileValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "PurposeOfEquipmentProfile_ValueStructure"
