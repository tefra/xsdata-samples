from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class MappedValueType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    is_reg_ex: None | bool = field(
        default=None,
        metadata={
            "name": "isRegEx",
            "type": "Attribute",
        },
    )
    start_index: None | int = field(
        default=None,
        metadata={
            "name": "startIndex",
            "type": "Attribute",
        },
    )
    end_index: None | int = field(
        default=None,
        metadata={
            "name": "endIndex",
            "type": "Attribute",
        },
    )
