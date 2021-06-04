from dataclasses import dataclass
from netex.models.place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OtherPlaceEquipment(PlaceEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
