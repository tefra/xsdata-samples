from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class LastModifiedDateTime:
    class Meta:
        name = "last-modified-date-time"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    format: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
