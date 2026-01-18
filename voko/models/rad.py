from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Rad:
    class Meta:
        name = "rad"

    var: None | str = field(
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
