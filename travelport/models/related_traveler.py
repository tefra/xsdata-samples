from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from travelport.models.loyalty_card_1 import LoyaltyCard1
from travelport.models.person_name import PersonName

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class RelatedTraveler:
    """
    Detailed related Traveler information for pre pay profiles.

    Parameters
    ----------
    loyalty_card
        Traveler loyalty card detail
    person_name
        Traveler name detail
    credits_used
        Traveler pre pay credit detail
    status_code
        Traveler status code(One of Marked for
        deletion,Lapsed,Terminated,Active,Inactive)
    relation
        Relation to the pre pay id. Example flight pass user
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    loyalty_card: list[LoyaltyCard1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    person_name: None | PersonName = field(
        default=None,
        metadata={
            "name": "PersonName",
            "type": "Element",
        },
    )
    credits_used: None | RelatedTraveler.CreditsUsed = field(
        default=None,
        metadata={
            "name": "CreditsUsed",
            "type": "Element",
        },
    )
    status_code: None | str = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Attribute",
        },
    )
    relation: None | str = field(
        default=None,
        metadata={
            "name": "Relation",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class CreditsUsed:
        used_credit: None | Decimal = field(
            default=None,
            metadata={
                "name": "UsedCredit",
                "type": "Attribute",
            },
        )
        currency_code: None | str = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Attribute",
                "length": 3,
            },
        )
