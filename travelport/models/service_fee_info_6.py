from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.credit_card_auth_6 import CreditCardAuth6
from travelport.models.form_of_payment_8 import FormOfPayment8
from travelport.models.payment_6 import Payment6
from travelport.models.service_fee_tax_info_6 import ServiceFeeTaxInfo6
from travelport.models.type_element_status_7 import TypeElementStatus7
from travelport.models.type_status_6 import TypeStatus6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class ServiceFeeInfo6:
    """
    Travel Agency Service Fees (TASF) are charged by the agency through BSP
    or Airline Reporting Corporation (ARC).

    Parameters
    ----------
    form_of_payment
    service_fee_tax_info
    credit_card_auth
    payment
    status
        Status of the service fee. Possible Values – Issued, ReadyToIssue,
        IssueLater.
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
    booking_traveler_name
        The name of the passenger.
    """

    class Meta:
        name = "ServiceFeeInfo"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    form_of_payment: None | FormOfPayment8 = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
        },
    )
    service_fee_tax_info: list[ServiceFeeTaxInfo6] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeTaxInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    credit_card_auth: None | CreditCardAuth6 = field(
        default=None,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
        },
    )
    payment: None | Payment6 = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
        },
    )
    status: None | TypeStatus6 = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
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
        },
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus7 = field(
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
    booking_traveler_name: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerName",
            "type": "Attribute",
        },
    )
