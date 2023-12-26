from dataclasses import dataclass, field
from typing import Optional


@dataclass
class UnitCode:
    class Meta:
        name = "@unit-code"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
