from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Percent:
    class Meta:
        name = "percent"

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
