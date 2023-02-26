from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ListName:
    class Meta:
        name = "@list-name"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
