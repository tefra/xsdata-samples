from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.payment_1 import Payment1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class RailUpdate:
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    booking_action: None | RailUpdate.BookingAction = field(
        default=None,
        metadata={
            "name": "BookingAction",
            "type": "Element",
            "required": True,
        },
    )
    reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )

    @dataclass
    class BookingAction:
        """
        Parameters
        ----------
        form_of_payment
        payment
        type_value
            the action associated with this booking. Four options are: Final
            (used to book with no ticket issuance) FinalTicket (used to book
            and issue ticket, default if FOP is included) Ticket (used to
            ticket an existing booking)
        """

        form_of_payment: None | FormOfPayment1 = field(
            default=None,
            metadata={
                "name": "FormOfPayment",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
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
        type_value: None | str = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
                "required": True,
            },
        )
