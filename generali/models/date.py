from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Date:
    class Meta:
        name = "date"

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
