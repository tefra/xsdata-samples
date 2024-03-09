from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.seat_attribute_2 import SeatAttribute2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class SeatAttributes2:
    """
    Identifies the seat attribute of the service.
    """

    class Meta:
        name = "SeatAttributes"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    seat_attribute: list[SeatAttribute2] = field(
        default_factory=list,
        metadata={
            "name": "SeatAttribute",
            "type": "Element",
            "max_occurs": 10,
        },
    )
