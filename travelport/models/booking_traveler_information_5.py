from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.name_5 import Name5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class BookingTravelerInformation5:
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
        namespace = "http://www.travelport.com/schema/common_v34_0"

    name: Name5 = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
