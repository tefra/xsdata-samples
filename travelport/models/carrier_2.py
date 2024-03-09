from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class Carrier2:
    """
    Carrier identifier.
    """

    class Meta:
        name = "Carrier"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
