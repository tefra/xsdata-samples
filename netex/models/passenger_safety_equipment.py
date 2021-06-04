from dataclasses import dataclass
from netex.models.passenger_safety_equipment_version_structure import PassengerSafetyEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerSafetyEquipment(PassengerSafetyEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
