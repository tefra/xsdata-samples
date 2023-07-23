from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_create_with_form_of_payment_req_1 import BaseCreateWithFormOfPaymentReq1
from travelport.models.host_token_list_1 import HostTokenList1
from travelport.models.payment_1 import Payment1
from travelport.models.rail_auto_seat_assignment import RailAutoSeatAssignment
from travelport.models.rail_exchange_solution import RailExchangeSolution
from travelport.models.rail_fare_note_list import RailFareNoteList

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailExchangeReq(BaseCreateWithFormOfPaymentReq1):
    """
    Creates a rail exchange reservation request with the host.

    Parameters
    ----------
    rail_exchange_solution
    payment
    rail_fare_note_list
        List of RailFareNote(s) that is referenced by key in RailFare.
    host_token_list
    rail_auto_seat_assignment
    locator_code
        The unique identifier for this rail reservation
    booking_action_type
        The action associated with this booking. Three options are:Final
        (used to book with no ticket issuance), FinalTicket (used to book
        and issue the ticket), Initiate (used for a provisional booking).
        Provider is RCH
    refund_option
        If the exchange results in money returned to the customer, ‘Refund’
        is sent to return the money to the original form or payment or
        ‘Retain’ is sent if the money should be returned in the form of an
        eVoucher for future use.  This attribute is supported by Amtrak/2V
        and ignored for all others.”
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_exchange_solution: None | RailExchangeSolution = field(
        default=None,
        metadata={
            "name": "RailExchangeSolution",
            "type": "Element",
        }
    )
    payment: None | Payment1 = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    rail_fare_note_list: None | RailFareNoteList = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
        }
    )
    host_token_list: None | HostTokenList1 = field(
        default=None,
        metadata={
            "name": "HostTokenList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    rail_auto_seat_assignment: list[RailAutoSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "RailAutoSeatAssignment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    locator_code: None | str = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    booking_action_type: None | str = field(
        default=None,
        metadata={
            "name": "BookingActionType",
            "type": "Attribute",
            "required": True,
        }
    )
    refund_option: None | str = field(
        default=None,
        metadata={
            "name": "RefundOption",
            "type": "Attribute",
        }
    )
