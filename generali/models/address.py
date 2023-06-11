from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Address:
    class Meta:
        name = "address"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
