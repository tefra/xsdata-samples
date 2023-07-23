from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.exchanged_coupon_1 import ExchangedCoupon1
from travelport.models.form_of_payment_1 import FormOfPayment1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class McoexchangeInfo1:
    """
    Information related to the exchange tickets available for the MCO.

    Parameters
    ----------
    form_of_payment
    exchanged_coupon
    original_ticket_number
        Airline form and serial number of the original ticket issued.
    original_city_code
        Location of honoring carrier or operator.
    original_ticket_date
        Date that the Original ticket was issued.
    iatacode
        IATA code of the issuing agency.
    """
    class Meta:
        name = "MCOExchangeInfo"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    form_of_payment: None | FormOfPayment1 = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
        }
    )
    exchanged_coupon: list[ExchangedCoupon1] = field(
        default_factory=list,
        metadata={
            "name": "ExchangedCoupon",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    original_ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "OriginalTicketNumber",
            "type": "Attribute",
            "length": 13,
        }
    )
    original_city_code: None | str = field(
        default=None,
        metadata={
            "name": "OriginalCityCode",
            "type": "Attribute",
            "length": 3,
        }
    )
    original_ticket_date: None | str = field(
        default=None,
        metadata={
            "name": "OriginalTicketDate",
            "type": "Attribute",
            "pattern": r"[^:Z].*",
        }
    )
    iatacode: None | str = field(
        default=None,
        metadata={
            "name": "IATACode",
            "type": "Attribute",
            "max_length": 8,
        }
    )
