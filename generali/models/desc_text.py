from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DescText:
    class Meta:
        name = "desc-text"

    type: Optional[str] = field(
        default=None,
        metadata={
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
