from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Find:
    class Meta:
        name = "find"

    href: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
