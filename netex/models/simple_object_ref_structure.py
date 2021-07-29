from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SimpleObjectRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
