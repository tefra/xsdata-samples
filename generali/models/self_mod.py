from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Self:
    class Meta:
        name = "self"

    href: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
