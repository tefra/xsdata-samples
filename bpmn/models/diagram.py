from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class Diagram:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    documentation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    resolution: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
