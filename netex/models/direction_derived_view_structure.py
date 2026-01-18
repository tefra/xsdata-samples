from dataclasses import dataclass, field
from typing import Optional

from .derived_view_structure import DerivedViewStructure
from .direction_ref import DirectionRef
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DirectionDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "Direction_DerivedViewStructure"

    direction_ref: DirectionRef | None = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
