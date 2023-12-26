from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_credit_card_type_5 import TypeCreditCardType5

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class CreditCard6(TypeCreditCardType5):
    """
    UProfile Specific Credit Card Element.

    Parameters
    ----------
    extract_indicator
        This is supported for all Profile Types by Universal Profile.This
        indicator will be used by MOS to create a Credit Card Extract.
    active
        Denotes whether the Credit Card is Active or Not.Default is true
    """

    class Meta:
        name = "CreditCard"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    extract_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "ExtractIndicator",
            "type": "Attribute",
        },
    )
    active: bool = field(
        default=True,
        metadata={
            "name": "Active",
            "type": "Attribute",
        },
    )
