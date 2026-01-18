from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Entry:
    class Meta:
        name = "entry"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
