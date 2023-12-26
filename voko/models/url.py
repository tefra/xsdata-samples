from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class Url:
    class Meta:
        name = "url"

    ref: Optional[str] = field(
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
