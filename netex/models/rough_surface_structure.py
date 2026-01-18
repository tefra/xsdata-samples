from __future__ import annotations

from dataclasses import dataclass, field

from .access_equipment_version_structure import AccessEquipmentVersionStructure
from .surface_type_enumeration import SurfaceTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoughSurfaceStructure(AccessEquipmentVersionStructure):
    surface_type: None | SurfaceTypeEnumeration = field(
        default=None,
        metadata={
            "name": "SurfaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    visual_contrast: None | bool = field(
        default=None,
        metadata={
            "name": "VisualContrast",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suitable_for_cycles: None | bool = field(
        default=None,
        metadata={
            "name": "SuitableForCycles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
