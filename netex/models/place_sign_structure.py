from dataclasses import dataclass, field
from typing import Optional

from .multilingual_string import MultilingualString
from .place_ref_1 import PlaceRef1
from .sign_equipment_version_structure import SignEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceSignStructure(SignEquipmentVersionStructure):
    place_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    place_ref: Optional[PlaceRef1] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
