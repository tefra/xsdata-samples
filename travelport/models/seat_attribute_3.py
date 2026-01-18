from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class SeatAttribute3:
    """
    Identifies the seat attribute of the service.
    """

    class Meta:
        name = "SeatAttribute"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    value: str = field(
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 2,
        }
    )
