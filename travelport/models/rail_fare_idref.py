from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailFareIdref:
    """
    Reference to a complete FareID from a shared list.
    """

    class Meta:
        name = "RailFareIDRef"
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
