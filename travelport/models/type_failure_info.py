from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeFailureInfo:
    class Meta:
        name = "typeFailureInfo"

    code: None | int = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    message: None | str = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
            "required": True,
        }
    )
