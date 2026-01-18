from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class Style:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
