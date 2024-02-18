from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class TypeFreeFormText5:
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
