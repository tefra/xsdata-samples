from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_req_seat import TypeReqSeat

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AutoSeatAssignment:
    """
    Request object used to request seats automatically by seat type.

    Parameters
    ----------
    segment_ref
        The segment that this assignment belongs to
    smoking
        Indicates that the requested seat type should be a smoking seat.
    seat_type
        The type of seat that is requested
    group
        Indicates that this seat request is for group seating for all
        passengers. If no SegmentRef is included, group seating will be
        requested for all segments.
    booking_traveler_ref
        The booking traveler that this seat assignment is for. If not
        entered, this applies to the primary booking traveler and other
        passengers are adjacent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )
    smoking: bool = field(
        default=False,
        metadata={
            "name": "Smoking",
            "type": "Attribute",
        }
    )
    seat_type: None | TypeReqSeat = field(
        default=None,
        metadata={
            "name": "SeatType",
            "type": "Attribute",
            "required": True,
        }
    )
    group: bool = field(
        default=False,
        metadata={
            "name": "Group",
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
