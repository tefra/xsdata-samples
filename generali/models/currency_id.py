from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CurrencyId:
    class Meta:
        name = "@currency-id"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
