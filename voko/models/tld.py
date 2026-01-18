from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Tld:
    class Meta:
        name = "tld"

    lit: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
