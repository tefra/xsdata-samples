from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ListAgencyName:
    class Meta:
        name = "@list-agency-name"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
