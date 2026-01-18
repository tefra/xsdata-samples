from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class Tld:
    class Meta:
        name = "tld"

    lit: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
