from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Url:
    class Meta:
        name = "url"

    ref: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
