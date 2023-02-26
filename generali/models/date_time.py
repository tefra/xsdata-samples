from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DateTime:
    class Meta:
        name = "date-time"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
