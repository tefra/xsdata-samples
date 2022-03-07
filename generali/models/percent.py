from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Percent:
    class Meta:
        name = "percent"

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
