from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Author:
    class Meta:
        name = "author"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
