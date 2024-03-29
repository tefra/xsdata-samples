from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CreatedDateTime:
    class Meta:
        name = "created-date-time"

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
