from __future__ import annotations
from dataclasses import dataclass
from travelport.models.seat_assignment_2 import SeatAssignment2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class AirSeatAssignment2(SeatAssignment2):
    """
    Identifies the seat assignment for a passenger.
    """

    class Meta:
        name = "AirSeatAssignment"
        namespace = "http://www.travelport.com/schema/common_v32_0"
