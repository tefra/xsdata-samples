from dataclasses import dataclass

from .place_equipment_ref_structure import PlaceEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessEquipmentRefStructure(PlaceEquipmentRefStructure):
    pass
