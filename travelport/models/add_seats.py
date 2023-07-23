from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.auto_seat_assignment import AutoSeatAssignment
from travelport.models.specific_seat_assignment import SpecificSeatAssignment

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class AddSeats:
    """
    Container for Seats to be added.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    auto_seat_assignment: list[AutoSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "AutoSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 20,
        }
    )
    specific_seat_assignment: list[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 20,
        }
    )
