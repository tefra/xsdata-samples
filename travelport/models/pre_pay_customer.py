from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.email_1 import Email1
from travelport.models.loyalty_card_1 import LoyaltyCard1
from travelport.models.person_name import PersonName
from travelport.models.related_traveler import RelatedTraveler
from travelport.models.type_structured_address_1 import TypeStructuredAddress1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PrePayCustomer:
    """
    Detailed customer information for searching pre pay profiles.

    Parameters
    ----------
    person_name
    email
        Customer email detail
    address
        Customer address detail
    related_traveler
        Travelers related to this pre pay id
    loyalty_card
        Customer loyalty card detail
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    person_name: None | PersonName = field(
        default=None,
        metadata={
            "name": "PersonName",
            "type": "Element",
        },
    )
    email: list[Email1] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    address: list[TypeStructuredAddress1] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    related_traveler: list[RelatedTraveler] = field(
        default_factory=list,
        metadata={
            "name": "RelatedTraveler",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    loyalty_card: list[LoyaltyCard1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
