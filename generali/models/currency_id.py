from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class CurrencyId:
    class Meta:
        name = "@currency-id"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
