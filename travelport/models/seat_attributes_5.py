from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.seat_attribute_5 import SeatAttribute5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class SeatAttributes5:
    """
    Identifies the seat attribute of the service.
    """

    class Meta:
        name = "SeatAttributes"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    seat_attribute: list[SeatAttribute5] = field(
        default_factory=list,
        metadata={
            "name": "SeatAttribute",
            "type": "Element",
            "max_occurs": 10,
        },
    )
