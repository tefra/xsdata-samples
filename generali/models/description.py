from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Description:
    class Meta:
        name = "description"

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
