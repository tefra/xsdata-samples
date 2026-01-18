from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class DescText:
    class Meta:
        name = "desc-text"

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
