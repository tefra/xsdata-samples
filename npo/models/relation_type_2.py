from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class RelationType2:
    class Meta:
        name = "relationType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    uri_ref: None | str = field(
        default=None,
        metadata={
            "name": "uriRef",
            "type": "Attribute",
        },
    )
    broadcaster: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
