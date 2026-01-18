from dataclasses import dataclass, field

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Reference:
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
