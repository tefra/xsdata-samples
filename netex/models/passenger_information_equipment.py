from dataclasses import dataclass
from netex.models.passenger_information_equipment_version_structure import PassengerInformationEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerInformationEquipment(PassengerInformationEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
