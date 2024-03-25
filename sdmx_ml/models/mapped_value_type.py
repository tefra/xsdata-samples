from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MappedValueType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    is_reg_ex: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isRegEx",
            "type": "Attribute",
        },
    )
    start_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "startIndex",
            "type": "Attribute",
        },
    )
    end_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "endIndex",
            "type": "Attribute",
        },
    )
