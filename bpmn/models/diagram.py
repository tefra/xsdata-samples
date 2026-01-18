from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class Diagram:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    documentation: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    resolution: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
