from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.name_1 import Name1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class PassengerInfo1:
    """
    Booking Traveler information tied to invoice.

    Parameters
    ----------
    name
    booking_traveler_ref
        A reference to a passenger related to a ticket.
    passenger_type
        Passenger Type Code.
    """

    class Meta:
        name = "PassengerInfo"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    name: None | Name1 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
    passenger_type: None | str = field(
        default=None,
        metadata={
            "name": "PassengerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        },
    )
