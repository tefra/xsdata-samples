from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class Provider1:
    """
    Provider identifier.
    """

    class Meta:
        name = "Provider"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
