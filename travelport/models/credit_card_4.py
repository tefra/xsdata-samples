from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_credit_card_type_4 import TypeCreditCardType4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class CreditCard4(TypeCreditCardType4):
    """
    Container for all credit card information.

    Parameters
    ----------
    profile_id
        The unique ID of the profile that contains the payment details to
        use.
    key
        The Key assigned to the payment details value from the specified
        profile.
    """

    class Meta:
        name = "CreditCard"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    profile_id: None | str = field(
        default=None,
        metadata={
            "name": "ProfileID",
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
