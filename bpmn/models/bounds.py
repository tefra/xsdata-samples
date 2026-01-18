from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DC"


@dataclass
class Bounds:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DC"

    x: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    width: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    height: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
