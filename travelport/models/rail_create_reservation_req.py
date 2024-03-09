from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_create_with_form_of_payment_req_1 import (
    BaseCreateWithFormOfPaymentReq1,
)
from travelport.models.host_token_list_1 import HostTokenList1
from travelport.models.payment_1 import Payment1
from travelport.models.rail_auto_seat_assignment import RailAutoSeatAssignment
from travelport.models.rail_fare_note_list import RailFareNoteList
from travelport.models.rail_pricing_solution import RailPricingSolution
from travelport.models.rail_specific_seat_assignment import (
    RailSpecificSeatAssignment,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class RailCreateReservationReq(BaseCreateWithFormOfPaymentReq1):
    """
    Creates a rail reservation with the host.

    Parameters
    ----------
    rail_pricing_solution
    payment
    rail_fare_note_list
        List of RailFareNote(s) that is referenced by key in RailFare.
    host_token_list
    rail_auto_seat_assignment
    rail_specific_seat_assignment
    booking_action_type
        the action associated with this booking. Four options are: Final
        (used to book with no ticket issuance) FinalTicket (used to book and
        issue ticket, default if FOP is included) Ticket (used to ticket an
        existing booking) Initiate (used for a provisional booking, default
        if no FOP is included)
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    rail_pricing_solution: None | RailPricingSolution = field(
        default=None,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "required": True,
        },
    )
    payment: None | Payment1 = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    rail_fare_note_list: None | RailFareNoteList = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
        },
    )
    host_token_list: None | HostTokenList1 = field(
        default=None,
        metadata={
            "name": "HostTokenList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    rail_auto_seat_assignment: list[RailAutoSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "RailAutoSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        },
    )
    rail_specific_seat_assignment: list[RailSpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "RailSpecificSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        },
    )
    booking_action_type: None | str = field(
        default=None,
        metadata={
            "name": "BookingActionType",
            "type": "Attribute",
            "required": True,
        },
    )
