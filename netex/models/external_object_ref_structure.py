from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ExternalObjectRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    ref: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
