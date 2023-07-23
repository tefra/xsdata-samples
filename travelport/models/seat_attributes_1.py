from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.seat_attribute_1 import SeatAttribute1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class SeatAttributes1:
    """
    Identifies the seat attribute of the service.
    """
    class Meta:
        name = "SeatAttributes"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    seat_attribute: list[SeatAttribute1] = field(
        default_factory=list,
        metadata={
            "name": "SeatAttribute",
            "type": "Element",
            "max_occurs": 10,
        }
    )
