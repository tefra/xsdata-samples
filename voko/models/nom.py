from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Nom:
    class Meta:
        name = "nom"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
