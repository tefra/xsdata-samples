from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassRefStructure:
    value: Optional[str] = field(
        default=None
    )
    name_of_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
            "required": True,
        }
    )
