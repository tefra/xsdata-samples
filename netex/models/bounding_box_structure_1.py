from __future__ import annotations

from dataclasses import dataclass, field

from .location_structure_1 import LocationStructure1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class BoundingBoxStructure1:
    class Meta:
        name = "BoundingBoxStructure"

    upper_left: LocationStructure1 = field(
        metadata={
            "name": "UpperLeft",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    lower_right: LocationStructure1 = field(
        metadata={
            "name": "LowerRight",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
