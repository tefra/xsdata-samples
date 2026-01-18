from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class NameText:
    class Meta:
        name = "name-text"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
