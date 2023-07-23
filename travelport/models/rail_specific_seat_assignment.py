from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailSpecificSeatAssignment:
    """
    Request object used to request a specific coach and seat number or a seat near-
    to a specific seat number.

    Parameters
    ----------
    coach_label
        The coach number of the train being requested.
    place_label
        The actual seat number or the close-to seat number based on the
        Assignment.
    assignment
        Defines how the PlaceLabel should be applied.  The values are
        6.STP for actual seat or 2.STP for close-to seat. Default is
        2.STP.
    rail_segment_ref
        The rail segment to which this assignment belongs.
    booking_traveler_ref
        The BookingTraveler for this seat assignment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    coach_label: None | str = field(
        default=None,
        metadata={
            "name": "CoachLabel",
            "type": "Attribute",
            "required": True,
        }
    )
    place_label: None | str = field(
        default=None,
        metadata={
            "name": "PlaceLabel",
            "type": "Attribute",
            "required": True,
        }
    )
    assignment: None | str = field(
        default=None,
        metadata={
            "name": "Assignment",
            "type": "Attribute",
            "required": True,
        }
    )
    rail_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "RailSegmentRef",
            "type": "Attribute",
            "required": True,
        }
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        }
    )
