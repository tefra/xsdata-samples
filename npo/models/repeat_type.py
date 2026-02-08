from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class RepeatType:
    class Meta:
        name = "repeatType"

    value: str = field(default="")
    is_rerun: bool = field(
        metadata={
            "name": "isRerun",
            "type": "Attribute",
        }
    )
