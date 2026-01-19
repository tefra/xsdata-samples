from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
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
