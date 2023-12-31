from dataclasses import dataclass, field
from typing import Optional
from .equipment_positions_rel_structure import EquipmentPositionsRelStructure
from .equipments_rel_structure import EquipmentsRelStructure
from .site_element_version_structure import SiteElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EquipmentPlaceVersionStructure(SiteElementVersionStructure):
    class Meta:
        name = "EquipmentPlace_VersionStructure"

    equipment_positions: Optional[EquipmentPositionsRelStructure] = field(
        default=None,
        metadata={
            "name": "equipmentPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    place_equipments: Optional[EquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
