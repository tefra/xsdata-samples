from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class Tezrad:
    class Meta:
        name = "tezrad"

    fak: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
