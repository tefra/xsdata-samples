from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinatesType:
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    decimal_value: str = field(
        default=".",
        metadata={
            "name": "decimal",
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
