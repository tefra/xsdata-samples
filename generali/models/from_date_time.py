from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FromDateTime:
    class Meta:
        name = "from-date-time"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    format: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
