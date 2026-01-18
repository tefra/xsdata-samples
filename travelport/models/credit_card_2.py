from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_credit_card_type_2 import TypeCreditCardType2

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class CreditCard2(TypeCreditCardType2):
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

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
