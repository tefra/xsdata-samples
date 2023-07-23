from __future__ import annotations
from dataclasses import dataclass
from travelport.models.seat_assignment_4 import SeatAssignment4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class AirSeatAssignment4(SeatAssignment4):
    """
    Identifies the seat assignment for a passenger.
    """
    class Meta:
        name = "AirSeatAssignment"
        namespace = "http://www.travelport.com/schema/common_v37_0"
