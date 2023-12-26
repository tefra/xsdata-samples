from __future__ import annotations
from dataclasses import dataclass
from travelport.models.seat_assignment_1 import SeatAssignment1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class AirSeatAssignment1(SeatAssignment1):
    """
    Identifies the seat assignment for a passenger.
    """

    class Meta:
        name = "AirSeatAssignment"
        namespace = "http://www.travelport.com/schema/common_v52_0"
