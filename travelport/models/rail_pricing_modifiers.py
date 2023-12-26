from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.discount_card_1 import DiscountCard1

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailPricingModifiers:
    """
    Search flexibiity criteria .

    Parameters
    ----------
    discount_card
        Discount request for rail.
    prohibit_non_refundable_fares
        Indicates whether it prohibits NonRefundable Fares.
    prohibit_non_exchangeable_fares
        Indicates whether it prohibits NonExchangeable Fares .
    currency_type
        3 Letter Currency Code
    rail_search_type
        RailSearchType options are "All Fares"  "Fastest"  "Lowest Fare"
        "One Fare Per Class" "Seasons".  Supported by NTV/VF only for "All
        Fares" "Lowest Fare" and "One Fare Per Class". Provider : RCH
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    discount_card: list[DiscountCard1] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 9,
        },
    )
    prohibit_non_refundable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonRefundableFares",
            "type": "Attribute",
        },
    )
    prohibit_non_exchangeable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonExchangeableFares",
            "type": "Attribute",
        },
    )
    currency_type: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "length": 3,
        },
    )
    rail_search_type: None | str = field(
        default=None,
        metadata={
            "name": "RailSearchType",
            "type": "Attribute",
        },
    )
