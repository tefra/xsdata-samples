from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Automatonstuff:
    class Meta:
        name = "automatonstuff"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
