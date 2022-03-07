from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Date:
    class Meta:
        name = "date"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    description: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
