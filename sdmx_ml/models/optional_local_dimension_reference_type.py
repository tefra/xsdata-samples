from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class OptionalLocalDimensionReferenceType:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_\-]*",
        },
    )
    optional: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
