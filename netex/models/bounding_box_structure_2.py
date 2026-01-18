from __future__ import annotations

from dataclasses import dataclass, field

from .location_structure_2 import LocationStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BoundingBoxStructure2:
    class Meta:
        name = "BoundingBoxStructure"

    upper_left: LocationStructure2 | None = field(
        default=None,
        metadata={
            "name": "UpperLeft",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    lower_right: LocationStructure2 | None = field(
        default=None,
        metadata={
            "name": "LowerRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
