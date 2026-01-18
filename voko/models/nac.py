from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Nac:
    class Meta:
        name = "nac"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
