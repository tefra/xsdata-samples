from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SimpleObjectRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    ref: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
