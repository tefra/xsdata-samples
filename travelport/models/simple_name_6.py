from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class SimpleName6:
    """
    Free text name.
    """

    class Meta:
        name = "SimpleName"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
