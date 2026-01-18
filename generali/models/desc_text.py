from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DescText:
    class Meta:
        name = "desc-text"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
