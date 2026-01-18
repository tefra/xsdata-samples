from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Vspec:
    class Meta:
        name = "vspec"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
