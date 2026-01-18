from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MultilingualString:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    text_id_type: None | str = field(
        default=None,
        metadata={
            "name": "textIdType",
            "type": "Attribute",
        },
    )
