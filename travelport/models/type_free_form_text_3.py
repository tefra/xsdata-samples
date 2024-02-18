from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class TypeFreeFormText3:
    """
    Free form Text.
    """

    class Meta:
        name = "typeFreeFormText"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
