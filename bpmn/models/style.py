from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class Style:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
