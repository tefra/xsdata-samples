from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class RelationType1:
    class Meta:
        name = "relationType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z0-9_-]{4,}",
        }
    )
    broadcaster: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    uri_ref: None | str = field(
        default=None,
        metadata={
            "name": "uriRef",
            "type": "Attribute",
        }
    )
    urn: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
