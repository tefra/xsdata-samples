from __future__ import annotations
from dataclasses import dataclass
from travelport.models.seat_assignment_3 import SeatAssignment3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class AirSeatAssignment3(SeatAssignment3):
    """
    Identifies the seat assignment for a passenger.
    """
    class Meta:
        name = "AirSeatAssignment"
        namespace = "http://www.travelport.com/schema/common_v33_0"
