from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Aut:
    class Meta:
        name = "aut"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
