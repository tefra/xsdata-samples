from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class UnitCode:
    class Meta:
        name = "@unit-code"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
