from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Numeric:
    class Meta:
        name = "numeric"

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
