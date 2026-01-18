from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass(kw_only=True)
class SectionType:
    class Meta:
        name = "sectionType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    path: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
