from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.add_seats import AddSeats
from travelport.models.booking_base_req import BookingBaseReq
from travelport.models.delete_seats import DeleteSeats
from travelport.models.update_seats import UpdateSeats

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingSeatAssignmentReq(BookingBaseReq):
    """
    Used to request auto or specific seat assignments.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_seats: None | AddSeats = field(
        default=None,
        metadata={
            "name": "AddSeats",
            "type": "Element",
        },
    )
    update_seats: None | UpdateSeats = field(
        default=None,
        metadata={
            "name": "UpdateSeats",
            "type": "Element",
        },
    )
    delete_seats: None | DeleteSeats = field(
        default=None,
        metadata={
            "name": "DeleteSeats",
            "type": "Element",
        },
    )
