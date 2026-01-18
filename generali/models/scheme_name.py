from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SchemeName:
    class Meta:
        name = "@scheme-name"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
