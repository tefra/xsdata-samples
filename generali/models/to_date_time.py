from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ToDateTime:
    class Meta:
        name = "to-date-time"

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
