from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DC"


@dataclass
class Bounds:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DC"

    x: float | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y: float | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    width: float | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    height: float | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
