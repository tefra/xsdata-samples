from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CodespaceRefStructure:
    value: Optional[str] = field(
        default=None
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
