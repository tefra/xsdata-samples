from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Self:
    class Meta:
        name = "self"

    href: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
