from dataclasses import dataclass, field
from typing import Optional
from .fuel_type_enumeration import FuelTypeEnumeration
from .place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RefuellingEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "RefuellingEquipment_VersionStructure"

    fuel_type: Optional[FuelTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FuelType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
