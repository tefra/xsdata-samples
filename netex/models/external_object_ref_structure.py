from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ExternalObjectRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    ref: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
