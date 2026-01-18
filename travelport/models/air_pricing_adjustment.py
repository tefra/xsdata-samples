from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.adjustment import Adjustment

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirPricingAdjustment:
    """
    This is a container to adjust price of AirPricingInfo.

    Pass zero values to remove existing adjustment.

    Parameters
    ----------
    adjustment
    key
        Key of AirPricingInfo from booking.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    adjustment: Adjustment = field(
        metadata={
            "name": "Adjustment",
            "type": "Element",
            "required": True,
        }
    )
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
