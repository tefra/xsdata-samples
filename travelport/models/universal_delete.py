from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_element import TypeElement

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class UniversalDelete:
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    element: TypeElement = field(
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
