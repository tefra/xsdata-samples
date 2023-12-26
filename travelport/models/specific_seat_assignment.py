from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SpecificSeatAssignment:
    """
    Request object used to specify a specific seat.

    Parameters
    ----------
    booking_traveler_ref
        The passenger that this seat assignment is for
    segment_ref
        The segment that we will assign this seat on
    flight_detail_ref
        The Flight Detail ref of the AirSegment used when requesting seats
        on Change of Guage flights
    seat_id
        The actual seat ID that is being requested. Special Characters are
        not supported in this field.
    rail_coach_number
        Coach number for which rail seatmap/coachmap is returned.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        },
    )
    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
            "required": True,
        },
    )
    flight_detail_ref: None | str = field(
        default=None,
        metadata={
            "name": "FlightDetailRef",
            "type": "Attribute",
        },
    )
    seat_id: None | str = field(
        default=None,
        metadata={
            "name": "SeatId",
            "type": "Attribute",
            "required": True,
        },
    )
    rail_coach_number: None | str = field(
        default=None,
        metadata={
            "name": "RailCoachNumber",
            "type": "Attribute",
            "max_length": 4,
        },
    )
