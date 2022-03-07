from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SchemeAgencyName:
    class Meta:
        name = "@scheme-agency-name"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
