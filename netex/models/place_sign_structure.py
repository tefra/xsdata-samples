from __future__ import annotations

from dataclasses import dataclass, field

from .multilingual_string import MultilingualString
from .place_ref import PlaceRef
from .sign_equipment_version_structure import SignEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceSignStructure(SignEquipmentVersionStructure):
    place_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    place_ref: None | PlaceRef = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
