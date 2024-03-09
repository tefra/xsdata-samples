from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_payment_card_3 import TypePaymentCard3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class DebitCard2(TypePaymentCard3):
    """
    Container for all debit card information.

    Parameters
    ----------
    issue_number
        Verification number for Debit Cards
    profile_id
        The unique ID of the profile that contains the payment details to
        use.
    key
        The Key assigned to the payment details value from the specified
        profile.
    """

    class Meta:
        name = "DebitCard"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    issue_number: None | str = field(
        default=None,
        metadata={
            "name": "IssueNumber",
            "type": "Attribute",
            "max_length": 8,
        },
    )
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
