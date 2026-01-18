from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class Rad:
    class Meta:
        name = "rad"

    var: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
