from dataclasses import dataclass

from .access_equipment_version_structure import AccessEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessEquipment(AccessEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
