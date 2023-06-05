from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class Tld:
    class Meta:
        name = "tld"

    lit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    var: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
