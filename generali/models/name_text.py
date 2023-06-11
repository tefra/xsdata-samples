from dataclasses import dataclass, field
from typing import Optional


@dataclass
class NameText:
    class Meta:
        name = "name-text"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
