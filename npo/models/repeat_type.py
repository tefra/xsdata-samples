from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class RepeatType:
    class Meta:
        name = "repeatType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    is_rerun: None | bool = field(
        default=None,
        metadata={
            "name": "isRerun",
            "type": "Attribute",
            "required": True,
        },
    )
