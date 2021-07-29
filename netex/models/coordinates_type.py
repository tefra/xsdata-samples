from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinatesType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
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
