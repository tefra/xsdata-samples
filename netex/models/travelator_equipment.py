from dataclasses import dataclass

from .travelator_equipment_version_structure import (
    TravelatorEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelatorEquipment(TravelatorEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
