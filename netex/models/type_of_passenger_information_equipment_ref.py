from dataclasses import dataclass

from .type_of_passenger_information_equipment_ref_structure import (
    TypeOfPassengerInformationEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfPassengerInformationEquipmentRef(
    TypeOfPassengerInformationEquipmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
