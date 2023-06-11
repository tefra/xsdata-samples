from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Duration:
    class Meta:
        name = "duration"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
