from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LastModifiedDateTime:
    class Meta:
        name = "last-modified-date-time"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
