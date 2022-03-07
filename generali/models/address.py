from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Address:
    class Meta:
        name = "address"

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
