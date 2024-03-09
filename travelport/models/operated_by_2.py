from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class OperatedBy2:
    """
    This is the carrier code to support Cross Accrual.
    """

    class Meta:
        name = "OperatedBy"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "white_space": "collapse",
        },
    )
