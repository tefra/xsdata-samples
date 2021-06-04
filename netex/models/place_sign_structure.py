from dataclasses import dataclass, field
from typing import Optional
from netex.models.multilingual_string import MultilingualString
from netex.models.place_ref_2 import PlaceRef2
from netex.models.sign_equipment_version_structure import SignEquipmentVersionStructure

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
        }
    )
    place_ref: Optional[PlaceRef2] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
