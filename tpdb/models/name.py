from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Name:
    class Meta:
        name = "name"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
