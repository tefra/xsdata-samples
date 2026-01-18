from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class OperatedBy3:
    """
    This is the carrier code to support Cross Accrual.
    """

    class Meta:
        name = "OperatedBy"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "white_space": "collapse",
        },
    )
