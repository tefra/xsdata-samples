from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Duration:
    class Meta:
        name = "duration"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
