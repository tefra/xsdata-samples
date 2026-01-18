from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CurrencyId:
    class Meta:
        name = "@currency-id"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
