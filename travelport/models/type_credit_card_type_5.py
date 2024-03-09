from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_payment_card_5 import TypePaymentCard5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class TypeCreditCardType5(TypePaymentCard5):
    """
    Parameters
    ----------
    extended_payment
        Used for American Express cards.
    customer_reference
        Agencies use this to pass the traveler information to the credit
        card company.
    acceptance_override
        Override airline restriction on the credit card.
    third_party_payment
        If true, this indicates that the credit card holder is not one of
        the passengers.
    bank_name
        Issuing bank name for this credit card
    bank_country_code
        ISO Country code associated with the issuing bank
    bank_state_code
        State code associated with the issuing bank.
    enett
        Acceptable values are true or false. If set to true it will denote
        that the credit card used has been issued through Enett. For all
        other credit card payments this value will be set to false.
    """

    class Meta:
        name = "typeCreditCardType"

    extended_payment: None | str = field(
        default=None,
        metadata={
            "name": "ExtendedPayment",
            "type": "Attribute",
        },
    )
    customer_reference: None | str = field(
        default=None,
        metadata={
            "name": "CustomerReference",
            "type": "Attribute",
        },
    )
    acceptance_override: None | bool = field(
        default=None,
        metadata={
            "name": "AcceptanceOverride",
            "type": "Attribute",
        },
    )
    third_party_payment: bool = field(
        default=False,
        metadata={
            "name": "ThirdPartyPayment",
            "type": "Attribute",
        },
    )
    bank_name: None | str = field(
        default=None,
        metadata={
            "name": "BankName",
            "type": "Attribute",
        },
    )
    bank_country_code: None | str = field(
        default=None,
        metadata={
            "name": "BankCountryCode",
            "type": "Attribute",
            "length": 2,
        },
    )
    bank_state_code: None | str = field(
        default=None,
        metadata={
            "name": "BankStateCode",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    enett: bool = field(
        default=False,
        metadata={
            "name": "Enett",
            "type": "Attribute",
        },
    )
