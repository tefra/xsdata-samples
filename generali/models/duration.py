from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Duration:
    class Meta:
        name = "duration"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )