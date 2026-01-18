from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.agency_info_1 import AgencyInfo1
from travelport.models.air_pricing_info import AirPricingInfo
from travelport.models.air_reservation_locator_code import (
    AirReservationLocatorCode,
)
from travelport.models.booking_traveler_1 import BookingTraveler1
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.passenger_ticket_number import PassengerTicketNumber
from travelport.models.payment_1 import Payment1
from travelport.models.refund_remark_1 import RefundRemark1
from travelport.models.supplier_locator_1 import SupplierLocator1
from travelport.models.type_tcrstatus import TypeTcrstatus

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Tcr:
    """
    Information related to Ticketless carriers.

    Parameters
    ----------
    form_of_payment
    payment
    booking_traveler
    passenger_ticket_number
    air_pricing_info
    agency_info
    air_reservation_locator_code
    supplier_locator
    refund_remark
    tcrnumber
        The identifying number for a Ticketless Air Reservation.
    status
        The current status of this TCR. Some status values are not
        applicable by some Airlines.
    modified_date
        The date at which the status was changed on this TCR due to an
        action event (itemized from the booleans below).
    confirmed_date
        The date at which this TCR was confirmed (not created). This mean
        the payment was approved and processed and travel for this TCR is
        confirmed.
    base_price
        The base price of this TCR as a whole as it was when it was first
        booked.
    taxes
        The taxes of this TCR as a whole as it was when it was first booked.
    fees
        The fees of this TCR as a whole as it was when it was first booked.
    refundable
        Is it possible to perform a Refund for this TCR.
    exchangeable
        Is it possible to perform an Exchange for this TCR.
    voidable
        Is it possible to perform a Void on this TCR.
    modifiable
        Is it possible to modify this TCR (opposed to Refund/Exchange/Void).
    provider_code
    provider_locator_code
    supplier_code
        Represents Carrier Code for ACH PNR Retrieve.
    refund_access_code
    refund_amount
        Total Amount refunded to the customer.
    refund_fee
        Charges incurred for processing refund.
    forfeit_amount
        Amount forfeited as a result of refund.
    """

    class Meta:
        name = "TCR"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    form_of_payment: list[FormOfPayment1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    payment: list[Payment1] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    booking_traveler: list[BookingTraveler1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    passenger_ticket_number: list[PassengerTicketNumber] = field(
        default_factory=list,
        metadata={
            "name": "PassengerTicketNumber",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_pricing_info: list[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    agency_info: None | AgencyInfo1 = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    air_reservation_locator_code: None | AirReservationLocatorCode = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
        },
    )
    supplier_locator: list[SupplierLocator1] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    refund_remark: list[RefundRemark1] = field(
        default_factory=list,
        metadata={
            "name": "RefundRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    tcrnumber: str = field(
        metadata={
            "name": "TCRNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    status: TypeTcrstatus = field(
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    modified_date: str = field(
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
            "required": True,
        }
    )
    confirmed_date: None | str = field(
        default=None,
        metadata={
            "name": "ConfirmedDate",
            "type": "Attribute",
        },
    )
    base_price: str = field(
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
            "required": True,
        }
    )
    taxes: str = field(
        metadata={
            "name": "Taxes",
            "type": "Attribute",
            "required": True,
        }
    )
    fees: str = field(
        metadata={
            "name": "Fees",
            "type": "Attribute",
            "required": True,
        }
    )
    refundable: bool = field(
        metadata={
            "name": "Refundable",
            "type": "Attribute",
            "required": True,
        }
    )
    exchangeable: bool = field(
        metadata={
            "name": "Exchangeable",
            "type": "Attribute",
            "required": True,
        }
    )
    voidable: bool = field(
        metadata={
            "name": "Voidable",
            "type": "Attribute",
            "required": True,
        }
    )
    modifiable: bool = field(
        metadata={
            "name": "Modifiable",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_code: str = field(
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: str = field(
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    refund_access_code: None | str = field(
        default=None,
        metadata={
            "name": "RefundAccessCode",
            "type": "Attribute",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_length": 1,
            "max_length": 32,
        },
    )
    refund_amount: None | str = field(
        default=None,
        metadata={
            "name": "RefundAmount",
            "type": "Attribute",
        },
    )
    refund_fee: None | str = field(
        default=None,
        metadata={
            "name": "RefundFee",
            "type": "Attribute",
        },
    )
    forfeit_amount: None | str = field(
        default=None,
        metadata={
            "name": "ForfeitAmount",
            "type": "Attribute",
        },
    )
