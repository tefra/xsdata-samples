from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.loyalty_program_1 import LoyaltyProgram1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AvailableDiscount:
    """
    Parameters
    ----------
    loyalty_program
        Customer Loyalty Program Detail.
    amount
    percent
    description
    discount_qualifier
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    loyalty_program: list[LoyaltyProgram1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyProgram",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    percent: None | str = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Attribute",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        },
    )
    discount_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "DiscountQualifier",
            "type": "Attribute",
        },
    )
