from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class AttributedUnsignedLongType:
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
