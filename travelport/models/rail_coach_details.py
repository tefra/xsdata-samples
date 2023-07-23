from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class RailCoachDetails:
    """
    Parameters
    ----------
    rail_coach_number
        Rail coach number for the returned coach details.
    available_rail_seats
        Number of available seats present in this rail coach.
    rail_seat_map_availability
        Indicates if seats are available in this rail coach which can be
        mapped.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    rail_coach_number: None | str = field(
        default=None,
        metadata={
            "name": "RailCoachNumber",
            "type": "Attribute",
        }
    )
    available_rail_seats: None | str = field(
        default=None,
        metadata={
            "name": "AvailableRailSeats",
            "type": "Attribute",
        }
    )
    rail_seat_map_availability: None | bool = field(
        default=None,
        metadata={
            "name": "RailSeatMapAvailability",
            "type": "Attribute",
        }
    )
