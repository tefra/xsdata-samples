from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Time:
    class Meta:
        name = "time"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    description: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
