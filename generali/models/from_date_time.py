from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FromDateTime:
    class Meta:
        name = "from-date-time"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
