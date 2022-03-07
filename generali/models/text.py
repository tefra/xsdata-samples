from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Text:
    class Meta:
        name = "text"

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
