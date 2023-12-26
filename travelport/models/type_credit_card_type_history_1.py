from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_payment_card_history_1 import (
    TypePaymentCardHistory1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeCreditCardTypeHistory1(TypePaymentCardHistory1):
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
    extract_indicator
        This is supported for all Profile Types by Universal Profile.This
        indicator will be used by MOS to create a Credit Card Extract.
    active
        Denotes whether the Credit Card is Active or Not.
    """

    class Meta:
        name = "typeCreditCardTypeHistory"

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
    extract_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "ExtractIndicator",
            "type": "Attribute",
        },
    )
    active: None | bool = field(
        default=None,
        metadata={
            "name": "Active",
            "type": "Attribute",
        },
    )
