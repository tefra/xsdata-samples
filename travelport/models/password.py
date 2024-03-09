from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/system_v32_0"


@dataclass
class Password:
    """
    Password Type.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    value: str = field(
        default="",
        metadata={
            "max_length": 32,
        },
    )
