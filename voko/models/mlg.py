from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class Mlg:
    class Meta:
        name = "mlg"

    kod: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
