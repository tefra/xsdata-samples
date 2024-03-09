from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class ProfileAssociation:
    """
    Profile information associated with SavedTrip.

    Parameters
    ----------
    traveler_id
        Traveler ID associated with saved Trip.
    booking_traveler_ref
        Booking Traveler associated with Profile.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    traveler_id: None | str = field(
        default=None,
        metadata={
            "name": "TravelerID",
            "type": "Attribute",
            "required": True,
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        },
    )
