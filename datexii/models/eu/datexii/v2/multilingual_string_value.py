from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class MultilingualStringValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 1024,
        },
    )
    lang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
