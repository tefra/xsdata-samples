from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Bib:
    class Meta:
        name = "bib"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
