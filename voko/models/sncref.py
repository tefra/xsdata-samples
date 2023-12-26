from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class Sncref:
    class Meta:
        name = "sncref"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
