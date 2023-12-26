from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.available_discount import AvailableDiscount
from travelport.models.baggage_restriction import BaggageRestriction

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BagDetails:
    """
    Information related to Bag details .

    Parameters
    ----------
    baggage_restriction
    available_discount
    applicable_bags
        Applicable baggage like Carry-On,1st Check-in,2nd Check -in etc.
    base_price
    approximate_base_price
    taxes
    total_price
    approximate_total_price
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    baggage_restriction: list[BaggageRestriction] = field(
        default_factory=list,
        metadata={
            "name": "BaggageRestriction",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    available_discount: list[AvailableDiscount] = field(
        default_factory=list,
        metadata={
            "name": "AvailableDiscount",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    applicable_bags: None | str = field(
        default=None,
        metadata={
            "name": "ApplicableBags",
            "type": "Attribute",
            "required": True,
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
