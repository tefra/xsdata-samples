from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Titolo:
    class Meta:
        name = "titolo"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
