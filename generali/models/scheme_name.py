from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SchemeName:
    class Meta:
        name = "@scheme-name"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
