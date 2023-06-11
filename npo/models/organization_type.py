from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class OrganizationType:
    class Meta:
        name = "organizationType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Z0-9_-]{2,}",
        }
    )
