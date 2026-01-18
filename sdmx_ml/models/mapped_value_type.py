from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MappedValueType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    is_reg_ex: bool | None = field(
        default=None,
        metadata={
            "name": "isRegEx",
            "type": "Attribute",
        },
    )
    start_index: int | None = field(
        default=None,
        metadata={
            "name": "startIndex",
            "type": "Attribute",
        },
    )
    end_index: int | None = field(
        default=None,
        metadata={
            "name": "endIndex",
            "type": "Attribute",
        },
    )
