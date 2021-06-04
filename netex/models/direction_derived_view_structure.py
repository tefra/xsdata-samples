from dataclasses import dataclass, field
from typing import Optional
from netex.models.derived_view_structure import DerivedViewStructure
from netex.models.direction_ref import DirectionRef
from netex.models.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DirectionDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "Direction_DerivedViewStructure"

    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
