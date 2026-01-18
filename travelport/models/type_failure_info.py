from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TypeFailureInfo:
    class Meta:
        name = "typeFailureInfo"

    code: int = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    message: str = field(
        metadata={
            "name": "Message",
            "type": "Attribute",
            "required": True,
        }
    )
