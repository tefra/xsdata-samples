from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Reference:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
