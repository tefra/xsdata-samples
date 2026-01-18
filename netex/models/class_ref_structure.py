from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    name_of_class: str | None = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
            "required": True,
        },
    )
