from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Text:
    class Meta:
        name = "text"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: object | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
