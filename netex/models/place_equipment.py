from dataclasses import dataclass

from .place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceEquipment(PlaceEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
