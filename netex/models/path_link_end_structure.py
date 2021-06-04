from dataclasses import dataclass, field
from typing import Optional
from netex.models.entrance_ref_structure import EntranceRefStructure
from netex.models.level_ref_structure import LevelRefStructure
from netex.models.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinkEndStructure:
    place_ref: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    level_ref: Optional[LevelRefStructure] = field(
        default=None,
        metadata={
            "name": "LevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_ref: Optional[EntranceRefStructure] = field(
        default=None,
        metadata={
            "name": "EntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
