from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class K:
    class Meta:
        name = "k"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
