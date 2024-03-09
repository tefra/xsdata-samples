from __future__ import annotations

from dataclasses import dataclass

from travelport.models.seat_assignment_5 import SeatAssignment5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class AirSeatAssignment5(SeatAssignment5):
    """
    Identifies the seat assignment for a passenger.
    """

    class Meta:
        name = "AirSeatAssignment"
        namespace = "http://www.travelport.com/schema/common_v34_0"
