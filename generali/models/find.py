from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Find:
    class Meta:
        name = "find"

    href: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
