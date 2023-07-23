from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.loyalty_card_details import LoyaltyCardDetails

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PassengerDetails:
    """
    Details of passenger.

    Parameters
    ----------
    loyalty_card_details
    key
        Passenger key
    code
        Passenger code
    age
        Passenger age
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    loyalty_card_details: list[LoyaltyCardDetails] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCardDetails",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 5,
        }
    )
    age: None | int = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        }
    )
