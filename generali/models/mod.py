from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Type:
    class Meta:
        name = "$"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
