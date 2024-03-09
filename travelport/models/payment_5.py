from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.payment_type_5 import PaymentType5
from travelport.models.type_element_status_6 import TypeElementStatus6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class Payment5:
    """Payment information - must be used in conjunction with credit card info

    Parameters
    ----------
    key
    type_value
        Identifies the type of payment. This can be for an itinerary, a
        traveler, or a service fee for example.
    form_of_payment_ref
        The credit card that is will be used to make this payment.
    booking_traveler_ref
        If the type represents a per traveler payment, then this will
        reference the traveler this payment refers to.
    amount
    amount_type
        This field displays type of payment amount when it is non-monetary.
        Presently available/supported value is "Flight Pass Credits".
    approximate_amount
        It stores the converted payment amount in agency's default currency
    status
        Status to indicate the business association of the payment element.
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        name = "Payment"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    type_value: None | PaymentType5 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    form_of_payment_ref: None | str = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Attribute",
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
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        },
    )
    amount_type: None | str = field(
        default=None,
        metadata={
            "name": "AmountType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
    approximate_amount: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateAmount",
            "type": "Attribute",
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus6 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
