from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinatesType:
    value: Optional[str] = field(
        default=None
    )
    decimal: str = field(
        default=".",
        metadata={
            "type": "Attribute",
        }
    )
    cs: str = field(
        default=",",
        metadata={
            "type": "Attribute",
        }
    )
    ts: str = field(
        default=" ",
        metadata={
            "type": "Attribute",
        }
    )
