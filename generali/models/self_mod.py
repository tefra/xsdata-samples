from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Self:
    class Meta:
        name = "self"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
