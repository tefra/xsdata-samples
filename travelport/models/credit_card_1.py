from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_credit_card_type_1 import TypeCreditCardType1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class CreditCard1(TypeCreditCardType1):
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
        namespace = "http://www.travelport.com/schema/common_v52_0"

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
