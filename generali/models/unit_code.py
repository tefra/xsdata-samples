from dataclasses import dataclass, field
from typing import Optional


@dataclass
class UnitCode:
    class Meta:
        name = "@unit-code"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
