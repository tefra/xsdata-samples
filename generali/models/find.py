from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Find:
    class Meta:
        name = "find"

    href: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
