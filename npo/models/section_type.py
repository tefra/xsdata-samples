from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class SectionType:
    class Meta:
        name = "sectionType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
