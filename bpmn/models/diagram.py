from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class Diagram:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    documentation: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    resolution: float | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
