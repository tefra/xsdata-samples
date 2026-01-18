from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DC"


@dataclass(kw_only=True)
class Bounds:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DC"

    x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    y: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    width: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    height: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
