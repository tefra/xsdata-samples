from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PrivateCodeStructure:
    value: Optional[str] = field(
        default=None
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
