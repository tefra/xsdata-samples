from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ListAgencyName:
    class Meta:
        name = "@list-agency-name"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
