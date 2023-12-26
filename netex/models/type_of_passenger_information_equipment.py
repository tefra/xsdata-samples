from dataclasses import dataclass
from .type_of_passenger_information_equipment_value_structure import (
    TypeOfPassengerInformationEquipmentValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfPassengerInformationEquipment(
    TypeOfPassengerInformationEquipmentValueStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
