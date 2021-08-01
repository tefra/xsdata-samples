from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MultilingualStringValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 1024,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
