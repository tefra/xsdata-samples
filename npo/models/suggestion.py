from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class Suggestion:
    class Meta:
        name = "suggestion"
        namespace = "urn:vpro:api:2013"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
