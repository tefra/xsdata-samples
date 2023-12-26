from dataclasses import dataclass, field
from typing import Optional
from .access_equipment_version_structure import AccessEquipmentVersionStructure
from .surface_type_enumeration import SurfaceTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoughSurfaceStructure(AccessEquipmentVersionStructure):
    surface_type: Optional[SurfaceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "SurfaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    suitable_for_cycles: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SuitableForCycles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
