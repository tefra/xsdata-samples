from dataclasses import dataclass, field

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VersionedReference:
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
