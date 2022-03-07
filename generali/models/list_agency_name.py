from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ListAgencyName:
    class Meta:
        name = "@list-agency-name"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
