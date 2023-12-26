from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.name_3 import Name3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class BookingTravelerInformation3:
    """
    Booking Traveler information tied to invoice.

    Parameters
    ----------
    name
    booking_traveler_ref
        A reference to a passenger related to a ticket.
    """

    class Meta:
        name = "BookingTravelerInformation"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    name: None | Name3 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
