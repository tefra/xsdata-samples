from dataclasses import dataclass, field
from typing import Optional
from .cycle_storage_enumeration import CycleStorageEnumeration
from .place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CycleStorageEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "CycleStorageEquipment_VersionStructure"

    number_of_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSpaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cycle_storage_type: Optional[CycleStorageEnumeration] = field(
        default=None,
        metadata={
            "name": "CycleStorageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    covered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
