from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class RedirectEntry:
    class Meta:
        name = "redirectEntry"
        namespace = "urn:vpro:api:2013"

    from_value: None | str = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
        },
    )
    to: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ultimate: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    circular: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
