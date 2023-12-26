from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.add_traveler import AddTraveler
from travelport.models.booking_base_req import BookingBaseReq
from travelport.models.delete_traveler import DeleteTraveler
from travelport.models.update_traveler import UpdateTraveler

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingTravelerReq(BookingBaseReq):
    """
    Used to add update delete booking traveler and its contents.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_traveler: None | AddTraveler = field(
        default=None,
        metadata={
            "name": "AddTraveler",
            "type": "Element",
        },
    )
    update_traveler: None | UpdateTraveler = field(
        default=None,
        metadata={
            "name": "UpdateTraveler",
            "type": "Element",
        },
    )
    delete_traveler: None | DeleteTraveler = field(
        default=None,
        metadata={
            "name": "DeleteTraveler",
            "type": "Element",
        },
    )
