from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.seat_attribute_6 import SeatAttribute6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class SeatAttributes6:
    """
    Identifies the seat attribute of the service.
    """

    class Meta:
        name = "SeatAttributes"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    seat_attribute: list[SeatAttribute6] = field(
        default_factory=list,
        metadata={
            "name": "SeatAttribute",
            "type": "Element",
            "max_occurs": 10,
        },
    )
