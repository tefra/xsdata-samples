from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailAutoSeatAssignment:
    """
    Request object used to request seats automatically by seat type.

    Parameters
    ----------
    seat_type
        Indicates codeset of values such as Seat Type like Place,Position,
        Smoking Choice, Place Arrangement, Place Direction, Compartment.
    seat_value
        Indicates the value specific to the selected type.
    rail_segment_ref
        The rail segment that this assignment belongs to
    booking_traveler_ref
        The booking traveler that this seat assignment is for. If not
        entered, this applies to the primary booking traveler and other
        passengers are adjacent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    seat_type: None | str = field(
        default=None,
        metadata={
            "name": "SeatType",
            "type": "Attribute",
            "required": True,
            "min_length": 0,
            "max_length": 255,
        }
    )
    seat_value: None | str = field(
        default=None,
        metadata={
            "name": "SeatValue",
            "type": "Attribute",
            "required": True,
            "min_length": 0,
            "max_length": 255,
        }
    )
    rail_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "RailSegmentRef",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
