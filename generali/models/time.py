from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Time:
    class Meta:
        name = "time"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
