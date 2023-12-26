from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class Characteristic8:
    """
    Identifies the characteristics of the seat with seat type, value and
    description.

    Parameters
    ----------
    seat_type
        Indicates codeset of values such as Seat Type like Place,Position,
        Smoking Choice, Place Arrangement, Place Direction, Compartment.
    seat_description
        Description of the seat type.
    seat_value
        Indicates the value specific to the selected type.
    seat_value_description
        Description of the seat value.
    """

    class Meta:
        name = "Characteristic"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    seat_type: None | str = field(
        default=None,
        metadata={
            "name": "SeatType",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
        },
    )
    seat_description: None | str = field(
        default=None,
        metadata={
            "name": "SeatDescription",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
        },
    )
    seat_value: None | str = field(
        default=None,
        metadata={
            "name": "SeatValue",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
        },
    )
    seat_value_description: None | str = field(
        default=None,
        metadata={
            "name": "SeatValueDescription",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
        },
    )
