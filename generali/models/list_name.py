from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ListName:
    class Meta:
        name = "@list-name"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
