from __future__ import annotations

from dataclasses import dataclass, field

from .access_equipment_version_structure import AccessEquipmentVersionStructure
from .lighting_enumeration import LightingEnumeration
from .lighting_on_method_enumeration import LightingOnMethodEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceLightingVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "PlaceLighting_VersionStructure"

    lighting: None | LightingEnumeration = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    always_lit: None | bool = field(
        default=None,
        metadata={
            "name": "AlwaysLit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lighting_on_method: None | LightingOnMethodEnumeration = field(
        default=None,
        metadata={
            "name": "LightingOnMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
