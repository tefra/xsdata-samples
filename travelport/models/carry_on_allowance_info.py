from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.baggage_restriction import BaggageRestriction
from travelport.models.base_baggage_allowance_info import (
    BaseBaggageAllowanceInfo,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class CarryOnAllowanceInfo(BaseBaggageAllowanceInfo):
    """
    Information related to Carry-On allowance like URL, pricing etc.

    Parameters
    ----------
    carry_on_details
        Information related to Carry-On Bag details .
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    carry_on_details: list[CarryOnAllowanceInfo.CarryOnDetails] = field(
        default_factory=list,
        metadata={
            "name": "CarryOnDetails",
            "type": "Element",
            "max_occurs": 999,
        },
    )

    @dataclass
    class CarryOnDetails:
        """
        Parameters
        ----------
        baggage_restriction
        applicable_carry_on_bags
            Applicable Carry-On baggage "First", "Second", "Third" etc
        base_price
        approximate_base_price
        taxes
        total_price
        approximate_total_price
        """

        baggage_restriction: list[BaggageRestriction] = field(
            default_factory=list,
            metadata={
                "name": "BaggageRestriction",
                "type": "Element",
                "max_occurs": 99,
            },
        )
        applicable_carry_on_bags: None | str = field(
            default=None,
            metadata={
                "name": "ApplicableCarryOnBags",
                "type": "Attribute",
            },
        )
        base_price: None | str = field(
            default=None,
            metadata={
                "name": "BasePrice",
                "type": "Attribute",
            },
        )
        approximate_base_price: None | str = field(
            default=None,
            metadata={
                "name": "ApproximateBasePrice",
                "type": "Attribute",
            },
        )
        taxes: None | str = field(
            default=None,
            metadata={
                "name": "Taxes",
                "type": "Attribute",
            },
        )
        total_price: None | str = field(
            default=None,
            metadata={
                "name": "TotalPrice",
                "type": "Attribute",
            },
        )
        approximate_total_price: None | str = field(
            default=None,
            metadata={
                "name": "ApproximateTotalPrice",
                "type": "Attribute",
            },
        )
