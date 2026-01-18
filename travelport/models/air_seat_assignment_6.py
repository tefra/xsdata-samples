from __future__ import annotations

from dataclasses import dataclass

from travelport.models.seat_assignment_6 import SeatAssignment6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class AirSeatAssignment6(SeatAssignment6):
    """
    Identifies the seat assignment for a passenger.
    """

    class Meta:
        name = "AirSeatAssignment"
        namespace = "http://www.travelport.com/schema/common_v38_0"
