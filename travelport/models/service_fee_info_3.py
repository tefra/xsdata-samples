from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.credit_card_auth_3 import CreditCardAuth3
from travelport.models.form_of_payment_4 import FormOfPayment4
from travelport.models.payment_3 import Payment3
from travelport.models.service_fee_tax_info_3 import ServiceFeeTaxInfo3
from travelport.models.type_element_status_4 import TypeElementStatus4
from travelport.models.type_status_3 import TypeStatus3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class ServiceFeeInfo3:
    """
    Travel Agency Service Fees (TASF) are charged by the agency through BSP or
    Airline Reporting Corporation (ARC).

    Parameters
    ----------
    form_of_payment
    service_fee_tax_info
    credit_card_auth
    payment
    status
    description
        The description of the service fee.
    key
    confirmation
        The confirmation number of the service fee in the merchant host
        system.
    ticket_number
        The ticket that this fee was issued in connection with.
    booking_traveler_ref
        A reference to a passenger.
    provider_reservation_info_ref
        A reference to the provider reservation info to which the service is
        tied.
    passive_provider_reservation_info_ref
        A reference to the passive provider reservation info to which the
        service is tied.
    total_amount
        The total amount for this Service Fee including base amount and all
        taxes.
    base_amount
        Represents the base price for this entity. This does not include any
        taxes.
    taxes
        The aggregated amount of all the taxes that are associated with this
        entity. See the associated Service Fee TaxInfo array for a breakdown
        of the individual taxes.
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
        name = "ServiceFeeInfo"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    form_of_payment: None | FormOfPayment4 = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
        },
    )
    service_fee_tax_info: list[ServiceFeeTaxInfo3] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeTaxInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    credit_card_auth: None | CreditCardAuth3 = field(
        default=None,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
        },
    )
    payment: None | Payment3 = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
        },
    )
    status: None | TypeStatus3 = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    confirmation: None | str = field(
        default=None,
        metadata={
            "name": "Confirmation",
            "type": "Attribute",
        },
    )
    ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
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
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    passive_provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "PassiveProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    total_amount: None | str = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Attribute",
        },
    )
    base_amount: None | str = field(
        default=None,
        metadata={
            "name": "BaseAmount",
            "type": "Attribute",
            "required": True,
        },
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus4 = field(
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
