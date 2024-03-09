from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.leg_detail import LegDetail

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class LegPrice:
    """
    Information about the journey Leg Price.

    Parameters
    ----------
    leg_detail
    key
    total_price
        The Total Prices for the Combination of Journey legs for this Price.
    approximate_total_price
        The Converted Total Price in Agency's Default Currency Value
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    leg_detail: list[LegDetail] = field(
        default_factory=list,
        metadata={
            "name": "LegDetail",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
    total_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
            "required": True,
        },
    )
    approximate_total_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        },
    )
