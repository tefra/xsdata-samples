from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Sncref:
    class Meta:
        name = "sncref"

    ref: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
